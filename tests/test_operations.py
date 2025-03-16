from src.math_operations import add, sub

def test_add():
    assert add(3, 2) == 5
    assert add(2, 1) == 3
    assert add(10, 9) == 19

def test_sub():
    assert sub(3, 2) == 1
    assert sub(2, 1) == 1
    assert sub(10, 9) == 1