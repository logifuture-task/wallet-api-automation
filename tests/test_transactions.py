import requests
import pytest
from utils.api_client import get_auth_token
from utils.config import BASE_URL


def test_wallet_transactions():
    """Test processing a transaction for a wallet."""
    token = get_auth_token()
    headers = {"Authorization": f"Bearer {token}"}
    wallet_id = "test-wallet-id"  # Replace with a valid wallet ID

    transaction_payload = {
        "amount": 100,
        "currency": "USD",
        "type": "deposit"
    }

    url = f"{BASE_URL}/wallet/{wallet_id}/transaction"
    response = requests.post(url, json=transaction_payload, headers=headers)

    assert response.status_code == 200, "Transaction failed"
    response_data = response.json()
    assert response_data.get("status") == "finished"
    assert response_data.get("outcome") == "approved"


def test_get_transaction():
    """Test retrieving a specific transaction."""
    token = get_auth_token()
    headers = {"Authorization": f"Bearer {token}"}
    wallet_id = "test-wallet-id"  # Replace with a valid wallet ID
    transaction_id = "test-transaction-id"  # Replace with a valid transaction ID

    url = f"{BASE_URL}/wallet/{wallet_id}/transaction/{transaction_id}"
    response = requests.get(url, headers=headers)

    assert response.status_code == 200, "Failed to retrieve transaction"
    response_data = response.json()
    assert response_data.get("transactionId") == transaction_id, "Transaction ID mismatch"


def test_get_all_transactions():
    """Test retrieving all transactions."""
    token = get_auth_token()
    headers = {"Authorization": f"Bearer {token}"}
    wallet_id = "test-wallet-id"  # Replace with a valid wallet ID

    url = f"{BASE_URL}/wallet/{wallet_id}/transactions"
    response = requests.get(url, headers=headers)

    assert response.status_code == 200, "Failed to retrieve transactions"
    response_data = response.json()
    assert "transactions" in response_data, "Transactions key missing in response"
