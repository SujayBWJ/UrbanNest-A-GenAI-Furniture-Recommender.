import pandas as pd
from pathlib import Path

def run_etl():
    BASE_DIR = Path(__file__).resolve().parent.parent

    products_path = BASE_DIR / "data" / "raw" / "products.csv"
    user_behavior_path = BASE_DIR / "data" / "raw" / "user_behavior.csv"

    products = pd.read_csv(products_path)
    user_behavior = pd.read_csv(user_behavior_path)

    products.columns = products.columns.str.lower()
    user_behavior.columns = user_behavior.columns.str.lower()

    products.drop_duplicates(inplace=True)
    user_behavior.drop_duplicates(inplace=True)

    if "price" in products.columns:
        products["price"].fillna(products["price"].median(), inplace=True)

    user_behavior["timestamp"] = pd.to_datetime(user_behavior["timestamp"])

    snapshot_date = user_behavior["timestamp"].max() + pd.Timedelta(days=1)

    rfm = user_behavior.groupby("user_id").agg({
        "timestamp": lambda x: (snapshot_date - x.max()).days,
        "product_id": "count"
    }).rename(columns={
        "timestamp": "recency",
        "product_id": "frequency"
    })

    monetary = user_behavior.merge(products, on="product_id") \
        .groupby("user_id")["price"].sum().rename("monetary")

    user_features = rfm.join(monetary)

    processed_dir = BASE_DIR / "data" / "processed"
    processed_dir.mkdir(parents=True, exist_ok=True)

    products.to_parquet(processed_dir / "products_clean.parquet", index=False)
    user_behavior.to_parquet(processed_dir / "user_behavior_clean.parquet", index=False)
    user_features.to_parquet(processed_dir / "user_features.parquet")

if __name__ == "__main__":
    run_etl()