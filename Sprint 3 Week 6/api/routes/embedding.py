from fastapi import APIRouter
from rag.retriever import FurnitureRetriever

router = APIRouter()

retriever = FurnitureRetriever()

@router.get("/embedding")
def embedding_recommend(query: str):

    results = retriever.retrieve_products(
        query,
        top_k=3
    )

    response = []

    for doc in results:

        response.append(
            {
                "product": doc.page_content
            }
        )

    return {
        "recommendations": response
    }