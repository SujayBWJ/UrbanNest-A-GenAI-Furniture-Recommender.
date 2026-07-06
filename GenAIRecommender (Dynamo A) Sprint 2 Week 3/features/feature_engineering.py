import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def load_data():
    path = BASE_DIR / "data" / "processed" / "user_behavior_clean.parquet"
    return pd.read_parquet(path)

def add_interaction_score(df):
    # No interaction_type available → treat each event equally
    df["score"] = 1
    return df

def aggregate_scores(df):
    return df.groupby(["user_id", "product_id"])["score"].sum().reset_index()

if __name__ == "__main__":
    df = load_data()
    df = add_interaction_score(df)
    df = aggregate_scores(df)
    print(df.head())