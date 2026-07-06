import pandas as pd
from pathlib import Path
from sklearn.metrics.pairwise import cosine_similarity

BASE_DIR = Path(__file__).resolve().parent.parent

def build_matrix():
    df = pd.read_parquet(BASE_DIR / "data/processed/user_behavior_clean.parquet")
    return pd.pivot_table(df, index="user_id", columns="product_id", aggfunc="size", fill_value=0)

def hybrid_recommend(user_id, top_n=5):
    matrix = build_matrix()

    similarity = cosine_similarity(matrix)
    sim_df = pd.DataFrame(similarity, index=matrix.index, columns=matrix.index)

    similar_users = sim_df[user_id].sort_values(ascending=False)[1:6].index

    scores = matrix.loc[similar_users].sum().sort_values(ascending=False)
    return scores.head(top_n)

if __name__ == "__main__":
    m = build_matrix()
    print(hybrid_recommend(m.index[0]))