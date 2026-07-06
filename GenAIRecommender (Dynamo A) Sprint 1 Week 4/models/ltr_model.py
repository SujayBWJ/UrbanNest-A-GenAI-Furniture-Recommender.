import pandas as pd
import numpy as np
from xgboost import XGBRanker

# -----------------------------
# DUMMY FEATURE DATA
# -----------------------------
np.random.seed(42)

data = pd.DataFrame({
    "cf_score": np.random.rand(100),
    "embedding_score": np.random.rand(100),
    "price_match": np.random.rand(100),
    "style_match": np.random.rand(100),
    "label": np.random.randint(0, 2, 100)
})

X = data[["cf_score", "embedding_score", "price_match", "style_match"]]
y = data["label"]

# group definition
groups = [20, 20, 20, 20, 20]

# -----------------------------
# TRAIN MODEL
# -----------------------------
model = XGBRanker(
    objective="rank:pairwise",
    learning_rate=0.1,
    max_depth=4,
    n_estimators=50
)

model.fit(X, y, group=groups)

# save model
import os

BASE_DIR = os.path.dirname(__file__)

checkpoint_dir = os.path.join(BASE_DIR, "model_checkpoints")
os.makedirs(checkpoint_dir, exist_ok=True)

model_path = os.path.join(checkpoint_dir, "ltr_model.json")

model.save_model(model_path)

print("LTR model trained successfully")