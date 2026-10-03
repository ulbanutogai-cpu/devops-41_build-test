import pytest
from app import multiply, divide

# Тест 1
def test_multiply():
    assert multiply(3, 4) == 12

# Тест 2
def test_divide():
    assert divide(10, 2) == 5

# Тест 3 (Проверка ошибки)
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
