from fastapi import APIRouter
from schemas import ChatRequest
from rag.rag_chain import qa_chain

router = APIRouter()

@router.post("/conversational")
def conversational_recommend(
    request: ChatRequest
):

    response = qa_chain.run(
        request.query
    )

    return {
        "response": response
    }