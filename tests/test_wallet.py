import requests
import pytest
from utils.api_client import get_auth_token
from utils.config import BASE_URL


def test_get_wallet():
    """Test retrieving wallet details."""
    token = get_auth_token()
    headers = {"Authorization": f"Bearer {token}"}
    wallet_id = "test-wallet-id"  # Replace with a valid wallet ID

    url = f"{BASE_URL}/wallet/{wallet_id}"
    response = requests.get(url, headers=headers)

    assert response.status_code == 200, "Failed to retrieve wallet"
    response_data = response.json()
    assert "balance" in response_data, "Balance key missing in response"
