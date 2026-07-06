import pandas as pd

products = pd.read_parquet("data/processed/products_clean.parquet")
users = pd.read_parquet("data/processed/user_features.parquet")

print(products.head())
print(users.head())

assert products.shape[0] > 0
assert users.shape[0] > 0

assert "product_id" in products.columns
assert "price" in products.columns

assert "recency" in users.columns
assert "frequency" in users.columns
assert "monetary" in users.columns

print("VALID")