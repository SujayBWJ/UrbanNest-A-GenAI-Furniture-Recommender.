# GENAI RECOMMENDER - SPRINT 1 WEEK 2

## Setup
Place raw data in:
data/raw/products.csv
data/raw/user_behavior.csv

## Run ETL
cd pipelines
python etl_pipeline.py

## Models
cd models
python popularity_model.py
python collaborative_filter.py
python matrix_factorization.py

## Evaluation
cd evaluation
python metrics.py

## Tests
cd tests
python test_recommenders.py

## Outputs
- Parquet files in data/processed/
- Recommendations from models