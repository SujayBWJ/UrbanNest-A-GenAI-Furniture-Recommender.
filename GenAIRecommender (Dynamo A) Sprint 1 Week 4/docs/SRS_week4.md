# Software Requirements Specification (SRS)

## Project Title

GenAI Hyper-Personalized Recommender System for UrbanNest Furnishings

---

## 1. Introduction

UrbanNest Furnishings aims to improve customer experience by implementing a personalized recommendation system capable of understanding customer preferences, browsing behavior, and purchase history.

---

## 2. Objective

The objective of this project is to build a hybrid recommender system using:
- Collaborative Filtering
- Content-Based Recommendation
- Embedding Similarity
- Learn-to-Rank Models

---

## 3. System Components

### ETL Pipeline
Responsible for:
- Data ingestion
- Data cleaning
- Feature engineering
- RFM calculation

### Collaborative Filtering Module
Generates recommendations using user-item interaction similarity.

### Embedding-Based Recommendation
Uses semantic similarity between product embeddings.

### Hybrid Recommender
Combines multiple recommendation signals into a unified ranking system.

### Learn-to-Rank Model
Uses ranking algorithms to optimize recommendation ordering.

---

## 4. Data Sources

### Product Dataset
Contains:
- Product attributes
- Price
- Style
- Material
- Ratings

### User Behavior Dataset
Contains:
- Views
- Cart additions
- Wishlist actions
- Purchases

---

## 5. Recommendation Workflow

1. Generate product embeddings
2. Build collaborative filtering scores
3. Retrieve content-based recommendations
4. Combine recommendation signals
5. Rank products using LTR model
6. Return Top-K recommendations

---

## 6. Technologies Used

- Python
- Pandas
- Scikit-learn
- XGBoost
- Sentence Transformers
- FAISS / ChromaDB

---

## 7. Constraints

- Synthetic dataset used
- Limited computational resources
- Basic evaluation metrics implemented

---

## 8. Expected Output

The system should:
- Recommend relevant furniture products
- Improve personalization
- Support semantic search
- Handle multiple recommendation signals

---

## 9. Conclusion

The recommender system provides a modular architecture for personalized product recommendation and forms the foundation for advanced GenAI-powered retail experiences.