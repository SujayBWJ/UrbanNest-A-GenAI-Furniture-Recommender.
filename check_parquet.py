import pandas as pd

df = pd.read_parquet("user_features.parquet")
print(df.head())