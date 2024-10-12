from app import random_fruit


def test_random_fruit():
    assert "apple" or "cherry" or "orange" or "banana" in random_fruit()
