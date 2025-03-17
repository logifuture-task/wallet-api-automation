import requests
import pytest
import threading
from utils.api_client import get_auth_token
from utils.config import BASE_URL


def test_concurrent_transactions():
    """Test multiple transactions happening at the same time."""

    def send_transaction():
        token = get_auth_token()
        headers = {"Authorization": f"Bearer {token}"}
        wallet_id = "test-wallet-id"
        transaction_payload = {"amount": 50, "currency": "USD", "type": "withdrawal"}
        url = f"{BASE_URL}/wallet/{wallet_id}/transaction"
        response = requests.post(url, json=transaction_payload, headers=headers)
        return response.status_code

    threads = [threading.Thread(target=send_transaction) for _ in range(5)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    assert any(
        send_transaction() == 400 for _ in range(5)), "At least one transaction should fail due to concurrency issues"


def test_large_transaction_amount():
    """Test processing an extremely large transaction amount."""
    token = get_auth_token()
    headers = {"Authorization": f"Bearer {token}"}
    wallet_id = "test-wallet-id"

    transaction_payload = {
        "amount": 1000000000,  # Unrealistically high amount
        "currency": "USD",
        "type": "deposit"
    }

    url = f"{BASE_URL}/wallet/{wallet_id}/transaction"
    response = requests.post(url, json=transaction_payload, headers=headers)

    assert response.status_code in [400, 422], "Large transactions should be restricted"


def test_transaction_with_high_frequency():
    """Test sending a large number of transactions in a short period."""
    token = get_auth_token()
    headers = {"Authorization": f"Bearer {token}"}
    wallet_id = "test-wallet-id"
    transaction_payload = {"amount": 10, "currency": "USD", "type": "deposit"}
    url = f"{BASE_URL}/wallet/{wallet_id}/transaction"

    responses = [requests.post(url, json=transaction_payload, headers=headers) for _ in range(50)]

    assert any(r.status_code == 429 for r in responses), "High-frequency transactions should trigger rate limits"


def test_transaction_with_long_decimal_amount():
    """Test processing a transaction with an excessive number of decimal places in amount."""
    token = get_auth_token()
    headers = {"Authorization": f"Bearer {token}"}
    wallet_id = "test-wallet-id"

    transaction_payload = {
        "amount": 100.123456789,  # Excessively long decimal places
        "currency": "USD",
        "type": "deposit"
    }

    url = f"{BASE_URL}/wallet/{wallet_id}/transaction"
    response = requests.post(url, json=transaction_payload, headers=headers)

    assert response.status_code in [400, 422], "Long decimal amounts should be restricted"


def test_transaction_with_zero_amount():
    """Test processing a transaction with zero amount."""
    token = get_auth_token()
    headers = {"Authorization": f"Bearer {token}"}
    wallet_id = "test-wallet-id"

    transaction_payload = {
        "amount": 0,
        "currency": "USD",
        "type": "deposit"
    }

    url = f"{BASE_URL}/wallet/{wallet_id}/transaction"
    response = requests.post(url, json=transaction_payload, headers=headers)

    assert response.status_code == 400, "Zero amount transactions should return 400"


def test_transaction_with_max_precision():
    """Test processing a transaction with the maximum allowed decimal precision."""
    token = get_auth_token()
    headers = {"Authorization": f"Bearer {token}"}
    wallet_id = "test-wallet-id"

    transaction_payload = {
        "amount": 100.1234,  # Assuming 4 decimal places are allowed
        "currency": "USD",
        "type": "deposit"
    }

    url = f"{BASE_URL}/wallet/{wallet_id}/transaction"
    response = requests.post(url, json=transaction_payload, headers=headers)

    assert response.status_code == 200, "Valid precision should be accepted"
