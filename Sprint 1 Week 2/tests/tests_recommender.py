from models.popularity_model import get_popular_products
from models.collaborative_filters import build_user_item_matrix
from models.matrix_factorization import run_svd
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))

def test_popularity():
    result = get_popular_products()
    assert len(result) > 0


def test_matrix():
    matrix = build_user_item_matrix()
    assert matrix.shape[0] > 0
    assert matrix.shape[1] > 0


def test_svd():
    latent = run_svd()
    assert latent.shape[0] > 0


if __name__ == "__main__":
    test_popularity()
    test_matrix()
    test_svd()
    print("All tests passed")