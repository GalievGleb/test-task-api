import pytest
import requests


class TestMainPage:

    def test_list_users(self):
        # Отправляем GET-запрос к указанному URL
        url = "https://reqres.in/api/users?page=2"
        response = requests.get(url)

        # Проверяем, что статус код ответа равен 200
        assert response.status_code == 200, "Expected status code 200"

        # Преобразуем ответ в формат JSON
        data = response.json()

        # Проверяем, что ключи 'page', 'per_page', 'total', 'total_pages' и 'data' есть в ответе
        assert "page" in data, "Key 'page' is not in the response"
        assert "per_page" in data, "Key 'per_page' is not in the response"
        assert "total" in data, "Key 'total' is not in the response"
        assert "total_pages" in data, "Key 'total_pages' is not in the response"
        assert "data" in data, "Key 'data' is not in the response"

        # Проверяем, что определенные 'id' есть в 'data'
        expected_ids = [7, 8, 9, 10, 11, 12]
        user_ids = [user["id"] for user in data["data"]]
        assert all(
            user_id in user_ids for user_id in expected_ids), f"Expected ids {expected_ids} not found in response"

    def test_single_user(self):
        # Отправляем GET-запрос к указанному URL
        url = "https://reqres.in/api/users/2"
        response = requests.get(url)

        # Проверяем, что статус код ответа равен 200
        assert response.status_code == 200, "Expected status code 200"

        # Преобразуем ответ в формат JSON
        data = response.json()

        # Проверяем наличие ожидаемых ключей в ответе
        expected_keys = ["data", "support"]
        assert all(key in data for key in expected_keys), f"Expected keys {expected_keys} not found in response"

        # Проверяем значения для ключа "data"
        data = data["data"]
        assert data["id"] == 2, "Expected id value is not equal to 2"
        assert data["email"] == "janet.weaver@reqres.in", "Email value is not as expected"
        assert data["first_name"] == "Janet", "First name is not as expected"
        assert data["last_name"] == "Weaver", "Last name is not as expected"
        assert data["avatar"] == "https://reqres.in/img/faces/2-image.jpg", "Avatar URL is not as expected"

    def test_single_user_not_found(self):
        # Отправляем GET-запрос к указанному URL
        url = "https://reqres.in/api/users/23"
        response = requests.get(url)

        # Проверяем, что статус код ответа равен 404
        assert response.status_code == 404, "Expected status code 404"

        # Проверяем, что ответ является пустым JSON-объектом
        assert response.json() == {}, "Expected an empty JSON response"

    def test_list_resource(self):
        # Отправляем GET-запрос к указанному URL
        url = "https://reqres.in/api/unknown"
        response = requests.get(url)

        # Проверяем, что статус код ответа равен 200
        assert response.status_code == 200, "Expected status code 200"

        # Парсим JSON-ответ
        json_response = response.json()

        # Проверяем ожидаемые значения в JSON-ответе
        assert json_response["page"] == 1, "Expected page value is not equal to 1"
        assert json_response["per_page"] == 6, "Expected per_page value is not equal to 6"
        assert json_response["total"] == 12, "Expected total value is not equal to 12"
        assert json_response["total_pages"] == 2, "Expected total_pages value is not equal to 2"

        # Проверяем значения в массиве "data"
        data = json_response["data"]
        assert len(data) == 6, "Expected 6 items in data array"

        # Пример проверки первого элемента в массиве "data"
        first_item = data[0]
        assert first_item["id"] == 1, "Expected id value for the first item is not equal to 1"
        assert first_item["name"] == "cerulean", "Expected name value for the first item is not equal to 'cerulean'"
        assert first_item["year"] == 2000, "Expected year value for the first item is not equal to 2000"
        assert first_item["color"] == "#98B2D1", "Expected color value for the first item is not equal to '#98B2D1'"
        assert first_item[
                   "pantone_value"] == "15-4020", "Expected pantone_value for the first item is not equal to '15-4020'"

        # Можете продолжить проверку для остальных элементов массива "data"

        # Проверяем значения в объекте "support"
        support = json_response["support"]
        assert support[
                   "url"] == "https://reqres.in/#support-heading", "Expected URL value in support is not as expected"
        assert support[
                   "text"] == "To keep ReqRes free, contributions towards server costs are appreciated!", "Expected text value in support is not as expected"

    def test_single_resource(self):
        # Отправляем GET-запрос к указанному URL
        url = "https://reqres.in/api/unknown/2"
        response = requests.get(url)

        # Проверяем, что статус код ответа равен 200
        assert response.status_code == 200, "Expected status code 200"

        # Парсим JSON-ответ
        json_response = response.json()

        # Проверяем ожидаемые значения в JSON-ответе
        data = json_response["data"]
        assert data["id"] == 2, "Expected id value is not equal to 2"
        assert data["name"] == "fuchsia rose", "Name value is not as expected"
        assert data["year"] == 2001, "Year value is not as expected"
        assert data["color"] == "#C74375", "Color value is not as expected"
        assert data["pantone_value"] == "17-2031", "Pantone value is not as expected"

        # Проверяем значения в объекте "support"
        support = json_response["support"]
        assert support[
                   "url"] == "https://reqres.in/#support-heading", "Expected URL value in support is not as expected"
        assert support[
                   "text"] == "To keep ReqRes free, contributions towards server costs are appreciated!", "Expected text value in support is not as expected"

    def test_single_resource_not_found(self):
        # Отправляем GET-запрос к указанному URL
        url = "https://reqres.in/api/unknown/23"
        response = requests.get(url)

        # Проверяем, что статус код ответа равен 404
        assert response.status_code == 404, "Expected status code 404"

        # Проверяем, что ответ является пустым JSON-объектом
        assert response.json() == {}, "Expected an empty JSON response"

    def test_create(self):
        # Задаем JSON-данные для отправки
        json_data = {
            "name": "morpheus",
            "job": "leader"
        }

        # Отправляем POST-запрос к указанному URL с JSON-данными
        url = "https://reqres.in/api/users"
        response = requests.post(url, json=json_data)

        # Проверяем, что статус код ответа равен 201 (Created)
        assert response.status_code == 201, "Expected status code 201"

        # Парсим JSON-ответ
        json_response = response.json()

        # Проверяем, что JSON-ответ содержит ожидаемые значения
        assert json_response["name"] == "morpheus", "Name value is not as expected"
        assert json_response["job"] == "leader", "Job value is not as expected"
        assert "id" in json_response, "ID is not present in the response"
        assert "createdAt" in json_response, "createdAt is not present in the response"

    def test_update_put(self):
        # Задаем JSON-данные для отправки
        json_data = {
            "name": "morpheus",
            "job": "zion resident"
        }

        # Отправляем PUT-запрос к указанному URL с JSON-данными
        url = "https://reqres.in/api/users/2"
        response = requests.put(url, json=json_data)

        # Проверяем, что статус код ответа равен 200 (OK)
        assert response.status_code == 200, "Expected status code 200"

        # Парсим JSON-ответ
        json_response = response.json()

        # Проверяем, что JSON-ответ содержит ожидаемые значения
        assert json_response["name"] == "morpheus", "Name value is not as expected"
        assert json_response["job"] == "zion resident", "Job value is not as expected"
        assert "updatedAt" in json_response, "updatedAt is not present in the response"

    def test_update_patch(self):
        # Задаем JSON-данные для отправки
        json_data = {
            "name": "morpheus",
            "job": "zion resident"
        }

        # Отправляем PUT-запрос к указанному URL с JSON-данными
        url = "https://reqres.in/api/users/2"
        response = requests.patch(url, json=json_data)

        # Проверяем, что статус код ответа равен 200 (OK)
        assert response.status_code == 200, "Expected status code 200"

        # Парсим JSON-ответ
        json_response = response.json()

        # Проверяем, что JSON-ответ содержит ожидаемые значения
        assert json_response["name"] == "morpheus", "Name value is not as expected"
        assert json_response["job"] == "zion resident", "Job value is not as expected"
        assert "updatedAt" in json_response, "updatedAt is not present in the response"

    def test_delete(self):
        # Отправляем DELETE-запрос к указанному URL
        url = "https://reqres.in/api/users/2"
        response = requests.delete(url)

        # Проверяем, что статус код ответа равен 204 (No Content)
        assert response.status_code == 204, "Expected status code 204"

        # Проверяем, что ответ не содержит контента (нет тела ответа)
        assert not response.content, "Expected empty response content"

    def test_register_successful(self):
        # Отправляем POST-запрос к указанному URL с данными для регистрации
        url = "https://reqres.in/api/register"
        data = {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }
        response = requests.post(url, json=data)

        # Проверяем, что статус код ответа равен 200 (OK)
        assert response.status_code == 200, "Expected status code 200"

        # Парсим JSON-ответ и проверяем наличие 'id' и 'token' в ответе
        json_response = response.json()
        assert 'id' in json_response, "Expected 'id' in response"
        assert 'token' in json_response, "Expected 'token' in response"

    def test_register_unsuccessful(self):
        # Отправляем POST-запрос к указанному URL без указания пароля
        url = "https://reqres.in/api/register"
        data = {
            "email": "sydney@fife"
        }
        response = requests.post(url, json=data)

        # Проверяем, что статус код ответа равен 400 (Bad Request)
        assert response.status_code == 400, "Expected status code 400"

        # Парсим JSON-ответ и проверяем, что в ответе есть поле 'error' с сообщением об ошибке
        json_response = response.json()
        assert 'error' in json_response, "Expected 'error' in response"
        assert json_response['error'] == "Missing password", "Expected 'Missing password' error message in response"

    def test_login_successful(self):
        # Отправляем POST-запрос к указанному URL с правильными учетными данными
        url = "https://reqres.in/api/login"
        data = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
        response = requests.post(url, json=data)

        # Проверяем, что статус код ответа равен 200 (OK)
        assert response.status_code == 200, "Expected status code 200"

        # Парсим JSON-ответ и проверяем, что в ответе есть поле 'token'
        json_response = response.json()
        assert 'token' in json_response, "Expected 'token' in response"

    def test_login_unsuccessful(self):
        # Отправляем POST-запрос к указанному URL с отсутствующим паролем
        url = "https://reqres.in/api/login"
        data = {
            "email": "peter@klaven"
        }
        response = requests.post(url, json=data)

        # Проверяем, что статус код ответа равен 400 (Bad Request)
        assert response.status_code == 400, "Expected status code 400"

        # Парсим JSON-ответ и проверяем, что в ответе есть поле 'error' с сообщением "Missing password"
        json_response = response.json()
        assert 'error' in json_response, "Expected 'error' in response"
        assert json_response['error'] == "Missing password", "Expected 'Missing password' error message"

    def test_delayed_response(self):
        # Отправляем GET-запрос к указанному URL с задержкой
        url = "https://reqres.in/api/users?delay=3"
        response = requests.get(url)

        # Проверяем, что статус код ответа равен 200 (OK)
        assert response.status_code == 200, "Expected status code 200"

        # Парсим JSON-ответ и проверяем его структуру и содержимое
        json_response = response.json()
        assert 'page' in json_response, "Expected 'page' in response"
        assert 'per_page' in json_response, "Expected 'per_page' in response"
        assert 'total' in json_response, "Expected 'total' in response"
        assert 'total_pages' in json_response, "Expected 'total_pages' in response"
        assert 'data' in json_response, "Expected 'data' in response"

        # Проверяем, что 'data' содержит список с ожидаемым количеством элементов (6)
        data = json_response['data']
        assert len(data) == 6, "Expected 6 items in 'data'"

        # Проверяем, что каждый элемент 'data' имеет ожидаемые ключи и значения
        for item in data:
            assert 'id' in item, "Expected 'id' in item"
            assert 'email' in item, "Expected 'email' in item"
            assert 'first_name' in item, "Expected 'first_name' in item"
            assert 'last_name' in item, "Expected 'last_name' in item"
            assert 'avatar' in item, "Expected 'avatar' in item"