from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import os


def create_pdf(path, title, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    doc = SimpleDocTemplate(path)
    styles = getSampleStyleSheet()

    elements = []
    elements.append(Paragraph(title, styles["Title"]))
    elements.append(Spacer(1, 12))

    for line in content.split("\n"):
        elements.append(Paragraph(line, styles["Normal"]))
        elements.append(Spacer(1, 8))

    doc.build(elements)


# ---------------- SRS ----------------
srs_content = """Software Requirements Specification (SRS) – Recommender System

1. Introduction
This document defines the requirements for a recommender system designed to suggest products based on user behavior data.
The system processes user interactions and generates personalized recommendations using multiple models.

2. System Overview
The system consists of:
- Data Processing (ETL Pipeline)
- Recommendation Models
- Evaluation Module

It operates entirely on local data without external dependencies.

3. Data Requirements

3.1 Input Data
- products.csv / products.parquet
- user_behavior.csv

3.2 Processed Data
- products_clean.parquet
- user_behavior_clean.parquet
- user_features.parquet

4. Functional Requirements

4.1 ETL Pipeline
- Read raw datasets
- Clean missing and duplicate values
- Convert timestamps
- Generate RFM features:
  - Recency
  - Frequency
  - Monetary

4.2 User-Item Matrix
- Construct matrix using purchase interactions
- Rows: users
- Columns: products
- Fill missing values with 0

4.3 Recommendation Models
- Popularity-Based Model
- User-Based Collaborative Filtering
- Item-Based Collaborative Filtering
- Matrix Factorization using SVD

4.4 Evaluation
- Precision@K implementation
- Basic evaluation reporting

5. Non-Functional Requirements
- Runs locally without external APIs
- Minimal dependencies (pandas, sklearn)
- Efficient processing for medium-sized datasets

6. System Constraints
- No real-time data streaming
- No GPU dependency
- Limited to offline batch processing

7. Assumptions
- User behavior data is available and clean
- Product IDs are consistent across datasets
- Interaction data reflects user preferences

8. Future Enhancements
- Hybrid recommendation system
- Integration with APIs for real-time use
- Incorporation of content-based features
- Scalable deployment architecture
"""

create_pdf("docs/SRS_Sprint1.pdf", "SRS - Sprint 1", srs_content)


# ---------------- Evaluation Report ----------------
eval_content = """Evaluation Report – Recommender System

1. Introduction
This report evaluates the performance of a recommender system built using user interaction data.
The system generates product recommendations using:
- Popularity-Based Recommendation
- Collaborative Filtering (User-Based)
- Matrix Factorization using SVD

The goal is to compare models and measure effectiveness.

2. Methodology

2.1 Data Preparation
The dataset consists of:
- products_clean.parquet
- user_behavior_clean.parquet

User interactions mapped as:
View = 1
Cart = 5
Purchase = 10

Only users with >5 interactions considered.

2.2 Train-Test Split
Training: 80%
Test: 20%

Example:
Train size: 23982
Test size: 5996

2.3 Evaluation Metrics
Precision@10
Recall@10
MAP@10

3. Results

Popularity:
Precision@10: 0.00643
Recall@10: 0.01873
MAP@10: 0.00606

Collaborative Filtering:
Precision@10: 0.00627
Recall@10: 0.01974
MAP@10: 0.00495

SVD Model:
Precision@10: 0.00606
Recall@10: 0.02095
MAP@10: 0.00670

4. Observations
- Popularity has highest precision
- SVD performs best in recall and MAP
- CF limited due to sparse data
- Metrics low due to implicit feedback
- Trade-off between precision and recall

5. Sample Recommendations

Collaborative Filtering:
Doctor Bed
Compare Bed
Election Wardrobe
Occur Table

SVD:
Doctor Bed
Family Bed
World Chair
Option Wardrobe

Popularity:
Detail Wardrobe
Magazine Sofa
Enjoy Table
Nature Wardrobe

6. Conclusion
- SVD gives best overall performance
- Popularity strong for global trends
- CF limited by sparsity

System successfully demonstrates a full pipeline.

7. Future Improvements
- Time-based splitting
- Hybrid models
- Better feature engineering
- Real-time API deployment
"""

create_pdf("evaluation/evaluation_report.pdf", "Evaluation Report - Sprint 1 Week 2", eval_content)