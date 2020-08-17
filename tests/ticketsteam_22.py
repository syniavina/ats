import pytest
import requests
from allure import issue, step, story
import logging


# 1. Получаем список билетов для абонемента в городе Postman с version_id (без auto_sale_linked_seat)
def test_ticket_season_list(url):
    place_id_in_sub = requests.get(url=f'{url}',
                                   params={"action": "ticket.season.list",
                                           "auth": "test_user:56a356e3d3b3e5e40ac1364b8a2b5cb42ccd6fbe:99999999999",
                                           "city_id": "41043",
                                           "season_id": "43683",
                                           "uid": "12345678901234567892",
                                           "version_id": "43569"}, verify=False).json()
    for place_id_sub in place_id_in_sub["result"]:
        if place_id_sub["id"] == 1017015:
            with step("place id в абонементе найден"):
                assert 1017015 == place_id_sub["id"],\
                    f"не найден place id для абонемента"


# 2. Получаем список всех мест для события “test_user event Big theatre”, которое входит в этот абонемент
def test_ticket_list(url):
    place_id_in_event = requests.get(url=f'{url}',
                                     params={"action": "ticket.list",
                                             "auth": "test_user:56a356e3d3b3e5e40ac1364b8a2b5cb42ccd6fbe:99999999999",
                                             "city_id": "41043",
                                             "event_id": "43687"}, verify=False).json()
    for place_id_event in place_id_in_event["result"]:
        if place_id_event["id"] == 1017087:
            with step("place id в событии найден"):
                assert 1017087 == place_id_event["id"],\
                    f"не найден place id для события"


# 3. Добавляем место из абонемента в корзину
def test_cart_season_add(url):
    cart_season_add_request = requests.get(url=f'{url}',
                                           params={"action": "cart.season.add",
                                                   "auth": "test_user:56a356e3d3b3e5e40ac1364b8a2b5cb42ccd6fbe:99999999999",
                                                   "city_id": "41043",
                                                   "id": "1017015",
                                                   "uid": "12345678901234567890"}, verify=False).json()
    with step("место из абонемента добавлено в корзину"):
        print(cart_season_add_request)
        assert cart_season_add_request["result"],\
            f"билет не добавлен в корзину"


# 4. Добавляем место из события в корзину. Проверяем текст ошибки.
def test_cart_add(url):
    cart_add_request = requests.get(url=f'{url}',
                                    params={"action": "cart.add",
                                            "auth": "test_user:56a356e3d3b3e5e40ac1364b8a2b5cb42ccd6fbe:99999999999",
                                            "city_id": "41043",
                                            "id": "1017087",
                                            "uid": "12345678901234567890"}, verify=False).json()
    with step("место из события НЕ добавлено в корзину"):
        logging.info(cart_add_request)
        assert cart_add_request["error"] == "Cart already has season places",\
            f"билет на событие добавлен в корзину, хотя не должен"


# 5. Удаляем место из корзины
def test_cart_season_remove(url):
    cart_season_remove_request = requests.get(url=f'{url}',
                                              params={"action": "cart.season.remove",
                                                      "auth": "test_user:56a356e3d3b3e5e40ac1364b8a2b5cb42ccd6fbe:99999999999",
                                                      "city_id": "41043",
                                                      "id": "1017015",
                                                      "uid": "12345678901234567890"}, verify=False).json()
    with step("место из абонемента добавлено в корзину"):
        print(cart_season_remove_request)
        assert cart_season_remove_request["result"],\
            f"билет удален из корзины"

