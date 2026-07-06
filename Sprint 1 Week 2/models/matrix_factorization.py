from pathlib import Path
import pandas as pd
from sklearn.decomposition import TruncatedSVD

BASE_DIR = Path(__file__).resolve().parent.parent

def run_svd(n_components=10):
    path = BASE_DIR / "data" / "processed" / "user_behavior_clean.parquet"
    df = pd.read_parquet(path)

    matrix = pd.pivot_table(
        df,
        index="user_id",
        columns="product_id",
        aggfunc="size",
        fill_value=0
    )

    svd = TruncatedSVD(n_components=n_components)
    latent = svd.fit_transform(matrix)

    return latent

if __name__ == "__main__":
    print(run_svd())