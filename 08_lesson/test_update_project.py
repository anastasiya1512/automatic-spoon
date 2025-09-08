import requests

base_url = "https://ru.yougile.com/"
api_key = "4V7hSUR2V0l+3Ubti0eJK7wA9FFRi5-BlgHpI0KLWv0s7dGQsJajpAqv+CoWqRgX"

headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }
body = {
    'title': "Новый проект - SkyPro"
}

body_negative = {
    'title': ""
}

body_update = {
    'title': "Update проект - SkyPro_New"
}


def test_update_project():
    resp = requests.post(
        f"{base_url}/api-v2/projects",
        headers=headers,
        json=body)

    new_id = resp.json().get('id')

    requests.put(
        f"{base_url}/api-v2/projects/f{new_id}",
        headers=headers,
        json=body_update)
    # Проверяем успешный статус создания
    assert resp.status_code == 201
    # Проверяем корректность созданных данных
    response_data = resp.json()
    assert 'id' in response_data


def test_update_project_negative():
    resp = requests.post(
        f"{base_url}/api-v2/projects",
        headers=headers,
        json=body
    )

    new_id = resp.json().get('id')
    resp = requests.put(
        f"{base_url}/api-v2/projects/f{new_id}",
        headers=headers, json=body_negative)
    # Проверяем статус ошибки обновления проекта (пустое тело запроса)
    assert resp.status_code == 400