def recall_at_k(actual, predicted, k=5):
    predicted = predicted[:k]
    return len(set(predicted) & set(actual)) / len(actual)

def map_at_k(actual, predicted, k=5):
    score = 0
    for i, p in enumerate(predicted[:k]):
        if p in actual:
            score += len(set(predicted[:i+1]) & set(actual)) / (i+1)
    return score / min(len(actual), k)

if __name__ == "__main__":
    actual = ["P1", "P2", "P3"]
    predicted = ["P1", "P4", "P2", "P5"]

    print("Recall@K:", recall_at_k(actual, predicted))
    print("MAP@K:", map_at_k(actual, predicted))