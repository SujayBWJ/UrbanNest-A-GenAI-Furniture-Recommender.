
# GenAI Hyper-Personalized Furniture Recommendation System

## Team Name
DynamoA

## Sprint
Sprint 3 - Week 5

## Overview
This project implements a Retrieval-Augmented Generation (RAG) based conversational recommendation engine for UrbanNest Furnishings.

The system combines:
- LangChain RAG Pipeline
- ChromaDB Vector Search
- Ollama + Llama 3
- Streamlit Conversational UI
- Personalized Recommendation Prompts
- Cross-sell & Up-sell Suggestions

## Features
- Personalized product recommendations
- Context-aware conversations
- Budget-based product filtering
- Style-aware recommendations
- Multi-turn conversational support
- Semantic similarity retrieval
- Vector embeddings using Sentence Transformers

## Folder Structure
- rag/ -> Retrieval pipeline
- llm/ -> LLM configuration
- ui/ -> Streamlit interface
- evaluation/ -> Evaluation metrics
- docs/ -> Architecture & SRS
- experiments/ -> Testing outputs
- notebooks/ -> Analysis notebook

## Setup
pip install -r requirements.txt

ollama pull llama3

streamlit run ui/chatbot_ui.py
