import pytest
from web.web_checks import check_form_submission

def test_form_submission(api_client, web_driver):
    check_form_submission(api_client, web_driver)
