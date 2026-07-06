import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def get_popular_products(top_n=10):
    path = BASE_DIR / "data" / "processed" / "user_behavior_clean.parquet"
    df = pd.read_parquet(path)

    popularity = (
        df.groupby("product_id")
        .size()
        .sort_values(ascending=False)
    )

    return popularity.head(top_n)

if __name__ == "__main__":
    print(get_popular_products())