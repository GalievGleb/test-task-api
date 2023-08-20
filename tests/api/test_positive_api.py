import pytest
import requests


class TestMainPage:
    def test_create(self):
        data = {
                "email": "eve.holt@reqres.in",
                "password": "pistol"
            }

        response1 = requests.post("https://reqres.in/api/register", data=data)

        assert "auth_sid" in response1.cookies, "There is no auth cookie in the response"
        assert "x-csrf-token" in response1.headers, "There is no CSRF in the response"
        assert "user_id" in response1.json, "There is no user id in the response"

        auth_sid = response1.cookies.get("auth_sid")
        token = response1.headers.get("x-csrf-token")
        user_id_from_auth_method = response1.json()["user_id"]

        # response2 = requests.get(
        #     ""
        # )