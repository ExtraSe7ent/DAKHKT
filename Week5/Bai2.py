import pytest

def is_prime(n):
    if n <= 1: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

@pytest.mark.parametrize('n, expected', [
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (17, True),
    (18, False),
    (19, True)
])
def test_is_prime(n, expected):
    assert is_prime(n) == expected