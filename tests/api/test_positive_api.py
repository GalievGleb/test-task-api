import pytest
from api.api_checks import check_positive_api_response


@pytest.mark.parametrize("page", [1, 2])
def test_positive_api_users(api_client, page):
    response = api_client.get_users(page)
    check_positive_api_response(response)
