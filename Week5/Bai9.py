import pytest

def safe_divide(a, b):
    if b == 0:
        return None
    return a / b

@pytest.mark.parametrize('a, b, expected', [
    (10, 2, 5.0),
    (5, 0, None),
    (-4, 2, -2.0)
])
def test_safe_divide(a, b, expected):
    assert safe_divide(a, b) == expected