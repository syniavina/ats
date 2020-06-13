import pytest
import requests
from allure import issue, step, story
import logging

def test_ticket_season_list(url):
    place_id_in_sub = requests.get(url=f'{url}',
                                   params={"action": "ticket.season.list",
                                           "auth": "test_user:56a356e3d3b3e5e40ac1364b8a2b5cb42ccd6fbe:99999999999",
                                           "city_id": "10592",
                                           "season_id": "28639",
                                           "uid": "12345678901234567890",
                                           "version_id": "23362"}, verify=False).json()
    for place_id_sub in place_id_in_sub["result"]:
        if place_id_sub["id"] == 842430:
            with step("place id в абонементе найден"):
                assert 842430 == place_id_sub["id"],\
                    f"не найден place id для абонемента"


def test_ticket_list(url):
    place_id_in_event = requests.get(url=f'{url}',
                                     params={"action": "ticket.list",
                                             "auth": "test_user:56a356e3d3b3e5e40ac1364b8a2b5cb42ccd6fbe:99999999999",
                                             "city_id": "10592",
                                             "event_id": "28635"}, verify=False).json()
    for place_id_event in place_id_in_event["result"]:
        if place_id_event["id"] == 841534:
            with step("place id в событии найден"):
                assert 841534 == place_id_event["id"],\
                    f"не найден place id для события"


def test_cart_season_add(url):
    cart_season_add_request = requests.get(url=f'{url}',
                                           params={"action": "cart.season.add",
                                                   "auth": "test_user:56a356e3d3b3e5e40ac1364b8a2b5cb42ccd6fbe:99999999999",
                                                   "city_id": "10592",
                                                   "id": "842430",
                                                   "uid": "12345678901234567890"}, verify=False).json()
    with step("место из абонемента добавлено в корзину"):
        print(cart_season_add_request)
        assert cart_season_add_request["result"],\
            f"билет не добавлен в корзину"


def test_cart_add(url):
    cart_add_request = requests.get(url=f'{url}',
                                    params={"action": "cart.add",
                                            "auth": "test_user:56a356e3d3b3e5e40ac1364b8a2b5cb42ccd6fbe:99999999999",
                                            "city_id": "10592",
                                            "id": "841534",
                                            "uid": "12345678901234567890"}, verify=False).json()
    with step("место из события НЕ добавлено в корзину"):
        logging.info(cart_add_request)
        assert cart_add_request["error"] == "Could not reserve a ticket",\
            f"билет на событие добавлен в корзину, хотя не должен"


def test_cart_season_remove(url):
    cart_season_remove_request = requests.get(url=f'{url}',
                                              params={"action": "cart.season.remove",
                                                      "auth": "test_user:56a356e3d3b3e5e40ac1364b8a2b5cb42ccd6fbe:99999999999",
                                                      "city_id": "10592",
                                                      "id": "842430",
                                                      "uid": "12345678901234567890"}, verify=False).json()
    with step("место из абонемента добавлено в корзину"):
        print(cart_season_remove_request)
        assert cart_season_remove_request["result"],\
            f"билет удален из корзины"

