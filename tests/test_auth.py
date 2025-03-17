import requests
import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.api_client import get_auth_token

def test_authentication():
    """Test user authentication."""
    token = get_auth_token()
    assert token is not None, "Token not received"
