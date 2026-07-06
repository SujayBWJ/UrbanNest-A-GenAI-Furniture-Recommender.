import pandas as pd

# -----------------------------
# LOAD DATA
# -----------------------------
products = pd.read_csv("products.csv")
behavior = pd.read_csv("user_behavior.csv")

# -----------------------------
# CLEANING
# -----------------------------
products.drop_duplicates(inplace=True)
behavior.drop_duplicates(inplace=True)

behavior["timestamp"] = pd.to_datetime(behavior["timestamp"])

# -----------------------------
# FILTER PURCHASES ONLY
# -----------------------------
purchases = behavior[behavior["event_type"] == "purchase"]

# merge to get price
merged = purchases.merge(products, on="product_id")

# -----------------------------
# RFM CALCULATION
# -----------------------------
snapshot_date = merged["timestamp"].max()

rfm = merged.groupby("user_id").agg({
    "timestamp": lambda x: (snapshot_date - x.max()).days,
    "user_id": "count",
    "price": "sum"
})

rfm.columns = ["Recency", "Frequency", "Monetary"]
rfm.reset_index(inplace=True)

# -----------------------------
# SAVE FILES
# -----------------------------
products.to_parquet("products_clean.parquet", index=False)
rfm.to_parquet("user_features.parquet", index=False)

print("Generated: products_clean.parquet, user_features.parquet")