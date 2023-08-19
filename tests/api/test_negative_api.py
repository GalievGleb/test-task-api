import pytest
from api.api_checks import check_negative_api_response

def test_negative_api_invalid_page(api_client):
    response = api_client.get_users(999)
    check_negative_api_response(response)
