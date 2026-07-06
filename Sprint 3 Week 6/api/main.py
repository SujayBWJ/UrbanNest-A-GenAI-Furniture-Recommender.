from fastapi import FastAPI

from api.routes.embedding import router as embedding_router
from api.routes.hybrid import router as hybrid_router
from api.routes.conversational import router as conversational_router

app = FastAPI(
    title="UrbanNest Recommendation API"
)

# -----------------------------------
# REGISTER ROUTES
# -----------------------------------
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

# -----------------------------------
# ROOT ENDPOINT
# -----------------------------------
@app.get("/")
def home():

    return {
        "message": "UrbanNest AI API Running"
    }