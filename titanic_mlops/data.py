import pandas as pd
from .config import load_config

cfg = load_config()

def load_and_clean(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    df = df[cfg["features"] + ["Survived"]].dropna()
    df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
    return df
