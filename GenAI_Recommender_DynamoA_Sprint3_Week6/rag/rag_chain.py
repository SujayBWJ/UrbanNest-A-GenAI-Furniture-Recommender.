from rag.retriever import FurnitureRetriever
import re

# The system architecture follows a RAG-style pipeline:
# - embeddings generated using SentenceTransformers MiniLM
# - ChromaDB used for vector retrieval
# - semantic search retrieves relevant products
# - conversational recommendation layer formats responses

# The original architecture included Llama3 via Ollama, but lightweight execution was prioritized due to local hardware constraints.

retriever = FurnitureRetriever()

# -----------------------------------
# CATEGORY SYNONYMS
# -----------------------------------
CATEGORY_MAP = {
    "sofa": ["sofa", "couch"],
    "table": ["table", "desk", "study table"],
    "chair": ["chair", "office chair"],
    "bed": ["bed"],
    "dining": ["dining", "dining table"]
}

# -----------------------------------
# DETECT CATEGORY
# -----------------------------------
def detect_category(query):

    query = query.lower()

    for category, keywords in CATEGORY_MAP.items():

        for keyword in keywords:

            if keyword in query:
                return category

    return None

# -----------------------------------
# DETECT PRICE
# -----------------------------------
def detect_max_price(query):

    match = re.search(
        r'under\s*[₹]?\s*(\d+)',
        query.lower()
    )

    if match:
        return int(match.group(1))

    return None

# -----------------------------------
# RESPONSE GENERATOR
# -----------------------------------
def generate_response(query):

    category = detect_category(query)

    max_price = detect_max_price(query)

    results = retriever.retrieve_products(query, top_k=15)

    filtered = []

    for doc in results:

        content = doc.page_content.lower()

        # -------------------------
        # STRICT CATEGORY FILTER
        # -------------------------
        if category:

            if category not in content:
                continue

        # -------------------------
        # PRICE FILTER
        # -------------------------
        if max_price:

            price_match = re.search(
                r'price:\s*(\d+)',
                content
            )

            if price_match:

                price = int(price_match.group(1))

                if price > max_price:
                    continue

        filtered.append(doc)

    # -----------------------------------
    # NO MATCH CASE
    # -----------------------------------
    if not filtered:

        return f"""
No exact products found for your query.

Try:
- increasing budget
- changing style
- broader furniture category
"""

    # -----------------------------------
    # FORMAT RESPONSE
    # -----------------------------------
    response = "Recommended Products:\n\n"

    for idx, doc in enumerate(filtered[:3], start=1):

        response += f"{idx}. {doc.page_content}\n\n"

    return response

# -----------------------------------
# QA CHAIN
# -----------------------------------
class MockQAChain:

    def run(self, query):
        return generate_response(query)

qa_chain = MockQAChain()