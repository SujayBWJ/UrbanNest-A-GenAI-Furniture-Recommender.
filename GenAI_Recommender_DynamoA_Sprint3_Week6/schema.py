from fastapi import FastAPI
from routes.embedding import router as embedding_router
from routes.hybrid import router as hybrid_router
from routes.conversational import router as conversational_router

app = FastAPI(
    title="UrbanNest Recommendation API"
)

app.include_router(
    embedding_router,
    prefix="/recommend"
)

app.include_router(
    hybrid_router,
    prefix="/recommend"
)

app.include_router(
    conversational_router,
    prefix="/recommend"
)

@app.get("/")
def home():

    return {
        "message": "UrbanNest AI API Running"
    }