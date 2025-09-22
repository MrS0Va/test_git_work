import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(1, 1) == 0

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 100) == 0

def test_divide():
    assert divide(10, 2) == 5
    assert divide(5, 2) == 2.5

def test_broken_test():
    assert add(2, 2) == 5 # Этот тест провалится

# Тест на проверку исключения
def test_divide_by_zero():
    with pytest.raises(ValueError, match="На ноль делить нельзя!"):
        divide(10, 0)