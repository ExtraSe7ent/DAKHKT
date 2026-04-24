import pytest

def calculate_tax(income):
    if income < 5000:
        return 0
    elif income < 10000:
        return income * 0.1
    else:
        return income * 0.2

@pytest.mark.parametrize('income, expected', [
    (3000, 0),
    (7000, 700.0),
    (12000, 2400.0)
])
def test_calculate_tax(income, expected):
    assert calculate_tax(income) == expected