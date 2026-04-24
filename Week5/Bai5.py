import requests
from unittest.mock import patch, MagicMock

def fetch_user():
    response = requests.get("https://api.example.com/user")
    return response.json()

def test_fetch_user():
    with patch('requests.get') as mock_get:
        mock_response = MagicMock()
        mock_response.json.return_value = {"id": 1, "name": "Quanganh"}
        mock_get.return_value = mock_response
        
        result = fetch_user()
        assert result == {"id": 1, "name": "Quanganh"}
        mock_get.assert_called_once_with("https://api.example.com/user")