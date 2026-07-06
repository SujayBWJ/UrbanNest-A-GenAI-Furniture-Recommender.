from fastapi import APIRouter

router = APIRouter()

@router.get("/hybrid")
def hybrid_recommend(query: str):

    return {
        "message": "Hybrid recommender active",
        "query": query
    }