from models.hybrid_recommender import hybrid_recommend, build_matrix

def test_hybrid():
    matrix = build_matrix()
    user = matrix.index[0]
    recs = hybrid_recommend(user)
    assert len(recs) > 0

if __name__ == "__main__":
    test_hybrid()
    print("All tests passed")