import os

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings


class FurnitureRetriever:

    def __init__(self):

        BASE_DIR = os.path.dirname(__file__)

        vector_db_path = os.path.join(BASE_DIR, 'vector_db')

        embedding_model = HuggingFaceEmbeddings(
            model_name='sentence-transformers/all-MiniLM-L6-v2'
        )

        self.vector_store = Chroma(
            persist_directory=vector_db_path,
            embedding_function=embedding_model
        )

    def retrieve_products(self, query, top_k=3):

        results = self.vector_store.similarity_search(
            query,
            k=top_k
        )

        return results