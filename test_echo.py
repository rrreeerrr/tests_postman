import allure 
import requests

@allure.title("Get-запрос с параметрами (Ivan, Moscow)")
@allure.description("Проверяем, чтобы сервер возвращал код ответа 200 и верные данные")
def test_get_with_params():
    url = "https://postman-echo.com/get?name=Ivan&city=Moscow"
    response = requests.get(url)

    assert response.status_code == 200

    info = response.json()

    assert info["args"]["name"] == "Ivan"
    assert info["args"]["city"] == "Moscow"

print("Успешно")

@allure.title("Post-запрос с данными (Elena, QA)")
@allure.description("Проверяем, что сервер принимает данные и возвращает код ответа 200")
def test_post():
    url = "https://postman-echo.com/post"
    
    my_data = {
        "name": "Elena",
        "course": "QA"
    }

    response = requests.post(url, json=my_data)

    assert response.status_code == 200

    info = response.json()

    assert info["data"]["name"] == "Elena"
    assert info["data"]["course"] == "QA"

print("Успешно")


@allure.title("Get-запрос с пустыми параметрами")
@allure.description("Проверяем, что запрос без данных обрабатывается и возвращает код ответа 200")
def test_get_empty():
    url = "https://postman-echo.com/get"
    response = requests.get(url)

    assert response.status_code == 200

    info = response.json()

    assert info["args"] == {}

print("Успешно")


@allure.title("Post-запрос с параметрами и телом")
@allure.description("Проверяем, что сервер принимает параметр status в URL и данные в теле, возвращает код 200")
def test_post_query():
    url = "https://postman-echo.com/post?status=success"
    my_data = {
        "letter": "Is it works?"
    }
    response = requests.post(url, json=my_data)
    
    assert response.status_code == 200
    
    info = response.json()
    
    assert info["args"]["status"] == "success"
    assert info["data"]["letter"] == "Is it works?"
    
print("Успешно")


@allure.title("Post-запрос с текстом")
@allure.description("Проверяем, что сервер принимает текст и возвращает код ответа 200")
def test_post_with_text():
    url = "https://postman-echo.com/post"
    my_text = "Просто текст"
    response = requests.post(url, data=my_text)

    assert response.status_code == 200

    info = response.json()

    assert info["data"] == "Просто текст"

print("Успешно")


@allure.title("Delete-запрос")
@allure.description("Проверяем, что сервер подтверждает удаление заметки и возвращает код ответа 200")
def test_delete():
    url = "https://postman-echo.com/delete"
    response = requests.delete(url)

    assert response.status_code == 200

    info = response.json()

    assert info["url"] == "https://postman-echo.com/delete"

print("Успешно")