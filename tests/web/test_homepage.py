import pytest
from web.web_checks import check_homepage

def test_homepage_load(web_driver):
    check_homepage(web_driver)
