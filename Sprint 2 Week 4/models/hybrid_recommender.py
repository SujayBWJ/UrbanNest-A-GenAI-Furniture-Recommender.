import numpy as np

# -----------------------------
# DUMMY SCORES
# -----------------------------
cf_scores = {
    "P001": 0.8,
    "P002": 0.6,
    "P003": 0.9
}

embedding_scores = {
    "P001": 0.7,
    "P002": 0.9,
    "P003": 0.5
}

price_match_scores = {
    "P001": 0.9,
    "P002": 0.4,
    "P003": 0.8
}

# -----------------------------
# HYBRID SCORING
# -----------------------------
final_scores = {}

for item in cf_scores:
    final_scores[item] = (
        0.4 * cf_scores[item] +
        0.4 * embedding_scores[item] +
        0.2 * price_match_scores[item]
    )

# rank
ranked = sorted(final_scores.items(),
                key=lambda x: x[1],
                reverse=True)

print("Top Recommendations:")
for item, score in ranked:
    print(item, round(score, 3))