
# System Architecture Notes

The project follows a simple RAG-based workflow.

1. User enters a furniture-related query in Streamlit UI.
2. Query is converted into embeddings.
3. ChromaDB retrieves similar product information.
4. Retrieved context is passed to Llama 3 through Ollama.
5. Final recommendation is shown to the user.

During implementation, retrieval quality improved after tuning similarity search parameters.
The system was tested locally on a standard laptop configuration.
