import requests

def test_get_with_params():
    url = "https://postman-echo.com/get?name=Ivan&city=Moscow"
    response = requests.get(url)

    assert response.status_code == 200

    info = response.json()

    assert info["args"]["name"] == "Ivan"
    assert info["args"]["city"] == "Moscow"

print("Успешно")


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


def test_get_empty():
    url = "https://postman-echo.com/get"
    response = requests.get(url)

    assert response.status_code == 200

    info = response.json()

    assert info["args"] == {}

print("Успешно")


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


def test_post_with_text():
    url = "https://postman-echo.com/post"
    my_text = "Просто текст"
    response = requests.post(url, data=my_text)

    assert response.status_code == 200

    info = response.json()

    assert info["data"] == "Просто текст"

print("Успешно")


def test_delete():
    url = "https://postman-echo.com/delete"
    response = requests.delete(url)

    assert response.status_code == 200

    info = response.json()

    assert info["url"] == "https://postman-echo.com/delete"

print("Успешно")