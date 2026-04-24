import pytest

def is_strong(password):
    return len(password) >= 8 and any(c.isdigit() for c in password)

@pytest.mark.parametrize('password, expected', [
    ("short1", False),
    ("no_digits_here", False),
    ("strongPass123", True)
])
def test_is_strong(password, expected):
    assert is_strong(password) == expected