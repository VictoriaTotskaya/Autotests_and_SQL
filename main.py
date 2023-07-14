# Виктория Тоцкая, 6-я когорта — Финальный проект. Инженер по тестированию плюс
import configuration
import data
import requests

def create_order(order_body, headers):
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                  json=order_body,
                  headers=headers)

    return response.json()["track"]

def get_order_response(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH + '?t=' + str(track))

def test_create_and_get_order():
    track = create_order(data.order_body, data.headers)
    order_response = get_order_response(track)

    assert order_response.status_code == 200