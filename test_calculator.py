from calculator import *


def test_add():
    """Test addition."""
    assert add(2, 3) == 5


def test_subtract():
    """Test subtraction."""
    assert subtract(5, 2) == 3


def test_multiply():
    """Test multiplication."""
    assert multiply(2, 4) == 8


def test_divide():
    """Test division."""
    assert divide(10, 2) == 5


def test_divide_by_zero():
    """Test divide by zero exception."""
    import pytest
    with pytest.raises(ValueError):
        divide(5, 0)
