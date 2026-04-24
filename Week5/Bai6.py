from datetime import datetime
from unittest.mock import patch

def is_weekend():
    today = datetime.now().weekday()
    return today >= 5

@patch('datetime.datetime')
def test_is_weekend(mock_datetime):
    mock_datetime.now.return_value.weekday.return_value = 4
    assert is_weekend() == False
    
    mock_datetime.now.return_value.weekday.return_value = 5
    assert is_weekend() == True