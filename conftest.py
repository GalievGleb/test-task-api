import pytest
from api.api_fixtures import api_client
from web.web_fixtures import web_driver

@pytest.fixture(scope="function")
def open_homepage(web_driver):
    # Открываем домашнюю страницу перед каждым тестом
    web_driver.get("https://example.com")  # Замените на свой URL

# ... другие фикстуры ...
