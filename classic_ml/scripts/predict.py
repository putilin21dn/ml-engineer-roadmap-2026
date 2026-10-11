import mlflow, yaml, os
import pandas as pd

config = yaml.safe_load(open("configs/config.yaml"))

tracking_uri = os.getenv("MLFLOW_TRACKING_URI", "sqlite:///mlflow.db")
model_name = os.getenv("MODEL_NAME", "churn-classifier")
model_alias = os.getenv("MODEL_ALIAS", "production")

model = None

def predict(X):
    global model
    if model is None:
        mlflow.set_tracking_uri(tracking_uri)
        model = mlflow.sklearn.load_model(f"models:/{model_name}@{model_alias}")

    X["TotalCharges"] = pd.to_numeric(X["TotalCharges"], errors="coerce")
    predict_proba = model.predict_proba(X)[:, 1]
    return (predict_proba > config["trashold"]).astype(int)

if __name__ == "__main__":
    test_data = pd.read_csv(config["test_path"])
    print(predict(test_data.iloc[:5]))
