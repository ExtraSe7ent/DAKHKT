import pytest

def clean_input(s):
    return s.strip().lower().replace(" ", "_")

@pytest.mark.parametrize('s, expected', [
    ("  hello  ", "hello"),
    ("UPPERCASE STRING", "uppercase_string"),
    ("  many   spaces  ", "many___spaces")
])
def test_clean_input(s, expected):
    assert clean_input(s) == expected