import os
import pandas as pd

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document

# -----------------------------
# LOAD DATASET
# -----------------------------
BASE_DIR = os.path.dirname(__file__)

csv_path = os.path.join(BASE_DIR, 'products.csv')

df = pd.read_csv(csv_path)

# -----------------------------
# CREATE PRODUCT DESCRIPTIONS
# -----------------------------
documents = []

for _, row in df.iterrows():

    text = f"""
    Product Name: {row.get('product_name', '')}
    Style: {row.get('style', '')}
    Price: {row.get('price', '')}
    Rating: {row.get('rating', '')}
    Stock: {row.get('stock', '')}
    """

    documents.append(
        Document(
            page_content=text,
            metadata={
                'product_id': row.get('product_id', ''),
                'style': row.get('style', '')
            }
        )
    )

# -----------------------------
# EMBEDDING MODEL
# -----------------------------
embedding_model = HuggingFaceEmbeddings(
    model_name='sentence-transformers/all-MiniLM-L6-v2'
)

# -----------------------------
# VECTOR DB PATH
# -----------------------------
vector_db_path = os.path.join(BASE_DIR, 'vector_db')

# -----------------------------
# CREATE VECTOR DATABASE
# -----------------------------
vector_store = Chroma.from_documents(
    documents=documents,
    embedding=embedding_model,
    persist_directory=vector_db_path
)

# -----------------------------
# SAVE VECTOR DATABASE
# -----------------------------
vector_store.persist()

print('Embeddings stored successfully')