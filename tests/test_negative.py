import requests
import pytest
from utils.api_client import get_auth_token
from utils.config import BASE_URL


def test_invalid_authentication():
    """Test authentication with invalid credentials."""
    url = f"{BASE_URL}/user/login"
    headers = {"X-Service-Id": "invalid-service-id"}
    payload = {"username": "wronguser", "password": "wrongpass"}

    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 401, "Invalid credentials should return 401"


def test_get_nonexistent_wallet():
    """Test retrieving a wallet that does not exist."""
    token = get_auth_token()
    headers = {"Authorization": f"Bearer {token}"}
    wallet_id = "nonexistent-wallet-id"

    url = f"{BASE_URL}/wallet/{wallet_id}"
    response = requests.get(url, headers=headers)

    assert response.status_code == 404, "Nonexistent wallet should return 404"


def test_wallet_transaction_insufficient_funds():
    """Test processing a withdrawal with insufficient funds."""
    token = get_auth_token()
    headers = {"Authorization": f"Bearer {token}"}
    wallet_id = "test-wallet-id"

    transaction_payload = {
        "amount": 1000000,  # Very large amount
        "currency": "USD",
        "type": "withdrawal"
    }

    url = f"{BASE_URL}/wallet/{wallet_id}/transaction"
    response = requests.post(url, json=transaction_payload, headers=headers)

    assert response.status_code == 400, "Insufficient funds should return 400"


def test_transaction_with_invalid_currency():
    """Test processing a transaction with an unsupported currency."""
    token = get_auth_token()
    headers = {"Authorization": f"Bearer {token}"}
    wallet_id = "test-wallet-id"

    transaction_payload = {
        "amount": 100,
        "currency": "XYZ",  # Unsupported currency
        "type": "deposit"
    }

    url = f"{BASE_URL}/wallet/{wallet_id}/transaction"
    response = requests.post(url, json=transaction_payload, headers=headers)

    assert response.status_code == 400, "Unsupported currency should return 400"


def test_transaction_with_negative_amount():
    """Test processing a transaction with a negative amount."""
    token = get_auth_token()
    headers = {"Authorization": f"Bearer {token}"}
    wallet_id = "test-wallet-id"

    transaction_payload = {
        "amount": -100,  # Negative amount should not be allowed
        "currency": "USD",
        "type": "deposit"
    }

    url = f"{BASE_URL}/wallet/{wallet_id}/transaction"
    response = requests.post(url, json=transaction_payload, headers=headers)

    assert response.status_code == 400, "Negative amount should return 400"


def test_wallet_access_without_authentication():
    """Test accessing wallet information without authentication."""
    wallet_id = "test-wallet-id"
    url = f"{BASE_URL}/wallet/{wallet_id}"
    response = requests.get(url)

    assert response.status_code == 401, "Unauthorized access should return 401"


def test_transaction_with_large_invalid_amount():
    """Test processing a transaction with an unreasonably large amount."""
    token = get_auth_token()
    headers = {"Authorization": f"Bearer {token}"}
    wallet_id = "test-wallet-id"

    transaction_payload = {
        "amount": 9999999999999,  # Very large amount should not be accepted
        "currency": "USD",
        "type": "deposit"
    }

    url = f"{BASE_URL}/wallet/{wallet_id}/transaction"
    response = requests.post(url, json=transaction_payload, headers=headers)

    assert response.status_code in [400, 422], "Unreasonably large transactions should be restricted"
