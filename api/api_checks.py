def check_positive_api_response(response):
    assert response.status_code == 200
    data = response.json()
    assert "page" in data
    assert "per_page" in data
    assert "total" in data
    assert "total_pages" in data
    assert "data" in data
    assert "support" in data


def check_negative_api_response(response):
    assert response.status_code == 404
