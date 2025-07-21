import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from .config import load_config

cfg = load_config()

def train(df):
    np.random.seed(cfg["seed"])
    X = df.drop("Survived", axis=1)
    y = df["Survived"]
    model = RandomForestClassifier(**cfg["model_params"])
    model.fit(X, y)
    return model

def save_model(model, path="model.pkl"):
    joblib.dump(model, path)
