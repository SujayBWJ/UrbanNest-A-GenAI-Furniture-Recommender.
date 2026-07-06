# WEEK 3

## Run Feature Engineering
python -m features.feature_engineering

## Run Hybrid Model
python -m models.hybrid_recommender

## Run API
uvicorn api.app:app --reload

## Test API
http://127.0.0.1:8000/recommend/<user_id>

## Run Tests
python -m tests.test_api