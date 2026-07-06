import pandas as pd
from pathlib import Path
from sklearn.metrics.pairwise import cosine_similarity

BASE_DIR = Path(__file__).resolve().parent.parent

def build_user_item_matrix():
    path = BASE_DIR / "data" / "processed" / "user_behavior_clean.parquet"
    df = pd.read_parquet(path)

    matrix = pd.pivot_table(
        df,
        index="user_id",
        columns="product_id",
        aggfunc="size",
        fill_value=0
    )
    return matrix

def user_based_cf(matrix, user_id):
    similarity = cosine_similarity(matrix)
    sim_df = pd.DataFrame(similarity, index=matrix.index, columns=matrix.index)
    return sim_df[user_id].sort_values(ascending=False).head(5)

def item_based_cf(matrix, product_id):
    similarity = cosine_similarity(matrix.T)
    sim_df = pd.DataFrame(similarity, index=matrix.columns, columns=matrix.columns)
    return sim_df[product_id].sort_values(ascending=False).head(5)

if __name__ == "__main__":
    m = build_user_item_matrix()
    print(user_based_cf(m, m.index[0]))
    print(item_based_cf(m, m.columns[0]))