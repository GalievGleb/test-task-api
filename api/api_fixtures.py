import pytest
import requests


@pytest.fixture(scope="function")
def api_client():
    base_url = "https://reqres.in/api"

    class APIClient:
        def get_users(self, page):
            response = requests.get(f"{base_url}/users", params={"page": page})
            return response

    return APIClient()
