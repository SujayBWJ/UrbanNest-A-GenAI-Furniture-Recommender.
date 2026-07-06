# 🛋️ UrbanNest: A GenAI Furniture Recommender

A modular recommendation system developed as part of an industry sprint project for **UrbanNest Furnishings**. The project progressively builds from synthetic data generation to hybrid recommendation models using collaborative filtering, content-based filtering, embeddings, and learning-to-rank techniques.

---

## 📌 Project Overview

UrbanNest Furnishings is a growing omnichannel furniture retailer looking to improve customer experience through personalized product recommendations.

This project implements a recommendation pipeline that evolves through multiple stages:

- Synthetic data generation
- Data cleaning & feature engineering
- Customer segmentation using RFM analysis
- Baseline recommender systems
- Embedding-based semantic search
- Vector database integration
- Hybrid recommendation engine
- Learn-to-Rank (LTR) model

---

## 🚀 Features

### Sprint 1 – Data Engineering & Baseline Models

- Synthetic product dataset generation
- Synthetic user behavior generation
- Data cleaning and preprocessing
- RFM (Recency, Frequency, Monetary) analysis
- ETL pipeline
- User-Item Interaction Matrix
- Popularity-Based Recommendation
- Collaborative Filtering
- Matrix Factorization
- Basic recommendation evaluation

### Sprint 2 – Embeddings & Hybrid Recommendation

- Product description generation
- Sentence embeddings
- Vector database integration
- Semantic similarity search
- Content-based recommendation
- Hybrid recommendation system
- Learn-to-Rank (LTR)
- Recommendation evaluation

---

## 🛠 Tech Stack

### Languages

- Python

### Libraries

- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Faker
- Sentence Transformers
- FAISS / ChromaDB

### Concepts

- ETL Pipeline
- Feature Engineering
- RFM Analysis
- Collaborative Filtering
- Matrix Factorization
- Vector Search
- Embeddings
- Hybrid Recommendation
- Learn-to-Rank

---

## 📂 Project Structure

```text
GenAI-Recommender/

├── data/
│   ├── raw/
│   └── processed/
│
├── pipelines/
│   └── etl_pipeline.py
│
├── models/
│   ├── popularity_model.py
│   ├── collaborative_filter.py
│   ├── matrix_factorization.py
│   ├── hybrid_recommender.py
│   ├── ltr_model.py
│   └── model_checkpoints/
│
├── evaluation/
│   ├── metrics.py
│   └── hybrid_evaluation_report.md
│
├── experiments/
│
├── docs/
│
├── notebooks/
│
└── README.md
```

---

## 📈 Recommendation Pipeline

```
Synthetic Data
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering (RFM)
      │
      ▼
User-Item Matrix
      │
      ▼
Baseline Recommenders
      │
      ├── Popularity Model
      ├── Collaborative Filtering
      └── Matrix Factorization
      │
      ▼
Sentence Embeddings
      │
      ▼
Vector Database
      │
      ▼
Semantic Search
      │
      ▼
Hybrid Recommendation
      │
      ▼
Learn-to-Rank
      │
      ▼
Final Recommendations
```

---

## 📊 Evaluation Metrics

The project evaluates recommendation quality using:

- Precision@K
- NDCG@K
- Similarity Scores
- Ranking Performance

---

## 🎯 Learning Outcomes

This project helped explore:

- Data engineering pipelines
- Feature engineering
- Customer segmentation
- Recommendation algorithms
- Embedding models
- Vector databases
- Hybrid recommender systems
- Learning-to-Rank models

---

## 🔮 Future Improvements

- Real customer datasets
- Real-time recommendation API
- Deep learning recommenders
- Reinforcement learning for personalization
- Session-based recommendations
- User feedback loop
- Production deployment

---

## 👨‍💻 Author

**Sujay Bharadwaj**

Computer Science and Business Systems (CSBS)

PES College of Engineering, Mandya

---

⭐ If you found this project interesting, consider giving it a star.
