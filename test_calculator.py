from calculator import add, subtract, multiply, power

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2

def test_multiply():
    assert multiply(5, 3) == 15

def test_power():
    assert power(2, 3) == 8