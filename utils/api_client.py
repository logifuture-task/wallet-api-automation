import requests
from utils.config import BASE_URL, SERVICE_ID, USERNAME, PASSWORD


def get_auth_token():
    """Authenticate and return a Bearer token."""
    url = f"{BASE_URL}/user/login"
    headers = {"X-Service-Id": SERVICE_ID}
    payload = {"username": USERNAME, "password": PASSWORD}

    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 200, "Authentication failed"
    return response.json().get("token")
