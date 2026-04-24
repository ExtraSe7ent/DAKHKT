from unittest.mock import patch

def send_welcome_email(email):
    print(f"Sending email to {email}")

def test_send_welcome_email():
    with patch('builtins.print') as mock_print:
        send_welcome_email("quanganh@example.com")
        mock_print.assert_called_once_with("Sending email to quanganh@example.com")