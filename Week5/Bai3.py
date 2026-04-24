import pytest

class User:
    def __init__(self, username):
        self.username = username

    def is_admin(self):
        return self.username == "admin"

@pytest.mark.parametrize('username, expected', [
    ('admin', True),
    ('guest', False),
    ('user123', False)
])
def test_user_is_admin(username, expected):
    user = User(username)
    assert user.is_admin() == expected