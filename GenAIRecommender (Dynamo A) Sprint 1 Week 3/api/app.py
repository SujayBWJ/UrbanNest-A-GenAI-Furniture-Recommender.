from fastapi import FastAPI
from models.hybrid_recommender import hybrid_recommend, build_matrix

app = FastAPI()
matrix = build_matrix()

@app.get("/")
def root():
    return {"message": "Recommender API Running"}

@app.get("/recommend/{user_id}")
def recommend(user_id: str):
    try:
        recs = hybrid_recommend(user_id)
        return {"user_id": user_id, "recommendations": recs.index.tolist()}
    except:
        return {"error": "User not found"}