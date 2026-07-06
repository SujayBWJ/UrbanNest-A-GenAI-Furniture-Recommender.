# UrbanNest API Documentation

## Base URL

http://localhost:8000

---

# Endpoints

## GET /

Health check endpoint.

Response:

{
  "message": "UrbanNest AI API Running"
}

---

# GET /recommend/embedding

Returns semantic recommendations.

Example:

/recommend/embedding?query=modern sofa

---

# GET /recommend/hybrid

Returns hybrid recommendation response.

Example:

/recommend/hybrid?query=luxury chair

---

# POST /recommend/conversational

Conversational RAG endpoint.

Request:

{
  "query": "Suggest Scandinavian sofas under 50000"
}

Response:

{
  "response": "..."
}