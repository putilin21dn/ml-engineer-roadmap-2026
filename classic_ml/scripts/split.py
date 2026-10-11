from sklearn.model_selection import train_test_split
import pandas as pd 

import kagglehub
import yaml

config = yaml.safe_load(open("configs/config.yaml"))

# загрузка из kaggle датасета
path = kagglehub.dataset_download(config["kaggle_path"])

df = pd.read_csv(path + "/" + config["kaggle_dataset"])

train_data, test_data = train_test_split(df, test_size=0.2, random_state=42, stratify=df["Churn"])

train_data.to_csv(config["train_path"], index=False)
test_data.to_csv(config["test_path"], index=False)