def precision_at_k(actual, predicted, k=5):
    predicted = predicted[:k]
    return len(set(predicted) & set(actual)) / k

if __name__ == "__main__":
    actual = [1, 2, 3]
    predicted = [1, 4, 5, 2, 6]
    print(precision_at_k(actual, predicted, k=3))