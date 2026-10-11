import pandas as pd
import yaml, os, joblib
import mlflow

from utils import _split_features

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.metrics import roc_auc_score,accuracy_score, f1_score, precision_score

from catboost import CatBoostClassifier

tracking_uri = os.getenv("MLFLOW_TRACKING_URI", "sqlite:///mlflow.db")
model_name = os.getenv("MODEL_NAME", "churn-classifier")
model_alias = os.getenv("MODEL_ALIAS", "production")


config = yaml.safe_load(open("configs/config.yaml"))
params = yaml.safe_load(open("configs/params.yaml"))

df = pd.read_csv(config["train_path"])

X,y = df.drop(columns=["customerID", "Churn"]), df["Churn"]

X["TotalCharges"] = pd.to_numeric(X["TotalCharges"], errors="coerce")

y = y.apply(lambda x: 1 if x == "Yes" else 0)

numeric, categorical, _ = _split_features(X, target="Churn")

numeric_steps = [("imputer", SimpleImputer(strategy="median"))]
numeric_transformer = Pipeline(steps=numeric_steps + [("scaler", StandardScaler())])

categorical_steps = [("imputer", SimpleImputer(strategy="most_frequent"))]
categorical_transformer = Pipeline(steps=categorical_steps + [("onehot", OneHotEncoder(handle_unknown="ignore"))])

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric),
        ("cat", categorical_transformer, categorical)
    ]
)

model = CatBoostClassifier(
    depth=params["depth"],
    iterations=params["iterations"],
    learning_rate=params["learning_rate"],
    verbose=params["verbose"],
    random_state=params["random_state"]
)

pipe = Pipeline([("preprocessor", preprocessor), ("model", model)])


model_dir = "models"
os.makedirs(model_dir, exist_ok=True)

pipe.fit(X, y)


joblib.dump(pipe, os.path.join(model_dir, "model.pkl"))

#считаем метрики на тесте
test_data = pd.read_csv(config["test_path"])

X_test, y_test = test_data.drop(columns=["customerID", "Churn"]), test_data["Churn"]
X_test["TotalCharges"] = pd.to_numeric(X_test["TotalCharges"], errors="coerce")

y_test = y_test.apply(lambda x: 1 if x == "Yes" else 0)

y_pred = pipe.predict(X_test)
y_proba = pipe.predict_proba(X_test)[:, 1]

mlflow.set_tracking_uri(tracking_uri)
mlflow.set_experiment("churn")

with mlflow.start_run(run_name=model_name) as run:
    mlflow.log_params(params)
    info = mlflow.sklearn.log_model(
        pipe,
        name="model",
        serialization_format="cloudpickle",
        registered_model_name=model_name,
    )
    mlflow.log_metrics({
        "roc_auc": roc_auc_score(y_test, y_proba),
        "accuracy": accuracy_score(y_test, y_pred),
        "f1": f1_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred)
    })
    client = mlflow.MlflowClient()
    client.set_registered_model_alias(
        model_name,
        model_alias,
        info.registered_model_version,
    )
