import pytest
import requests
from allure import issue, step, story
import logging


# 1. Получаем список билетов для абонемента в городе Postman с auto_sale_linked_seat = true
def test_ticket_season_list_auto(url):
    place_id_in_sub_with_auto = requests.get(url=f'{url}',
                                             params={"action": "ticket.season.list",
                                                     "auth": "test_user:56a356e3d3b3e5e40ac1364b8a2b5cb42ccd6fbe:99999999999",
                                                     "city_id": "41043",
                                                     "season_id": "43690",
                                                     "uid": "12345678901234567893",
                                                     "auto_sale_linked_seat": "true"}, verify=False).json()
    for place_id_sub_auto in place_id_in_sub_with_auto["result"]:
        if place_id_sub_auto["id"] == 1017123:
            with step("place id в абонементе найден"):
                assert 1017123 == place_id_sub_auto["id"],\
                    f"не найден place id для абонемента"


# 2. Добавляем в корзину место 1017123 c auto_sale_linked_seat = true
def test_cart_season_add_auto(url):
    cart_season_add_request_auto = requests.get(url=f'{url}',
                                                params={"action": "cart.season.add",
                                                        "auth": "test_user:56a356e3d3b3e5e40ac1364b8a2b5cb42ccd6fbe:99999999999",
                                                        "city_id": "41043",
                                                        "id": "1017123",
                                                        "uid": "12345678901234567893",
                                                        "auto_sale_linked_seat": "true"}, verify=False).json()
    with step("место из абонемента добавлено в корзину вместе со связанным"):
        print(cart_season_add_request_auto)
        assert cart_season_add_request_auto["result"],\
            f"билет не добавлен в корзину"


# 3. Добавляем в корзину место 1017124 c version_id = 43569 (Барвиха)
def test_cart_season_add_first_hall(url):
    cart_season_add_first_hall_request = requests.get(url=f'{url}',
                                                      params={"action": "cart.season.add",
                                                              "auth": "test_user:56a356e3d3b3e5e40ac1364b8a2b5cb42ccd6fbe:99999999999",
                                                              "city_id": "41043",
                                                              "id": "1017124",
                                                              "uid": "12345678901234567893",
                                                              "version_id": "43569"}, verify=False).json()
    with step("место из абонемента НЕ может быть добавлено повторно в корзину"):
        logging.info(cart_season_add_first_hall_request)
        assert cart_season_add_first_hall_request["error"] == "Error while add to cart",\
            f"билет добавлен в корзину, хотя не должен"


# 4. Удаляем места из корзины с auto_sale_linked_seat=true
def test_cart_season_remove_auto(url):
    cart_season_remove_request = requests.get(url=f'{url}',
                                              params={"action": "cart.season.remove",
                                                      "auth": "test_user:56a356e3d3b3e5e40ac1364b8a2b5cb42ccd6fbe:99999999999",
                                                      "city_id": "41043",
                                                      "id": "1017123",
                                                      "uid": "12345678901234567893",
                                                      "auto_sale_linked_seat": "true"}, verify=False).json()
    with step("место из абонемента удалено из корзины вместе со связанным"):
        print(cart_season_remove_request)
        assert cart_season_remove_request["result"],\
            f"билет НЕ удален из корзины"


# 5. Добавляем место из абонемента без auto_sale_linked_seat, но с версией зала Барвихи
def test_cart_season_add_first_hall(url):
    cart_season_add_first_hall_request = requests.get(url=f'{url}',
                                                      params={"action": "cart.season.add",
                                                              "auth": "test_user:56a356e3d3b3e5e40ac1364b8a2b5cb42ccd6fbe:99999999999",
                                                              "city_id": "41043",
                                                              "id": "1017124",
                                                              "uid": "12345678901234567893",
                                                              "version_id": "43569"}, verify=False).json()
    with step("место из первого зала добавлено в корзину"):
        print(cart_season_add_first_hall_request)
        assert cart_season_add_first_hall_request["result"], \
            f"билет НЕ добавлен в корзину"


# 6. Проверяем, что место из второго зала (Главклуб) доступно к выбору
def test_ticket_season_list_second_hall(url):
    place_id_in_sub_second_hall = requests.get(url=f'{url}',
                                               params={"action": "ticket.season.list",
                                                       "auth": "test_user:56a356e3d3b3e5e40ac1364b8a2b5cb42ccd6fbe:99999999999",
                                                       "city_id": "41043",
                                                       "season_id": "43690",
                                                       "uid": "12345678901234567893",
                                                       "version_id": "43661"}, verify=False).json()
    for place_id_in_sub_second_hall_tickets in place_id_in_sub_second_hall["result"]:
        if place_id_in_sub_second_hall_tickets["id"] == 1023327:
            with step("place id в абонементе найден"):
                assert 1023327 == place_id_in_sub_second_hall_tickets["id"],\
                    f"не найден place id для абонемента"


# 7. Добавляем место из абонемента без auto_sale_linked_seat, но с версией зала ГлавClub
def test_cart_season_add_second_hall(url):
    cart_season_add_second_hall_request = requests.get(url=f'{url}',
                                                       params={"action": "cart.season.add",
                                                               "auth": "test_user:56a356e3d3b3e5e40ac1364b8a2b5cb42ccd6fbe:99999999999",
                                                               "city_id": "41043",
                                                               "id": "1023327",
                                                               "uid": "12345678901234567893",
                                                               "version_id": "43661"}, verify=False).json()
    with step("место из второго зала добавлено в корзину"):
        print(cart_season_add_second_hall_request)
        assert cart_season_add_second_hall_request["result"], \
            f"билет НЕ добавлен в корзину"


# 8. Создаем заказ
def test_order_season_create(url):
    order_season_create = requests.get(url=f'{url}',
                                       params={"action": "order.create",
                                               "auth": "test_user:56a356e3d3b3e5e40ac1364b8a2b5cb42ccd6fbe:99999999999",
                                               "uid": "12345678901234567893",
                                               "city_id": "41043",
                                               "name": "Oksana",
                                               "phone": "+7 (000) 000-00-01"}, verify=False).json()
    with step("заказ создан"):
        print(order_season_create)
        assert order_season_create["result"], \
            f"заказ не создан"


# 9. Продаем заказ
def test_order_season_sold(url):
    order_season_sold = requests.get(url=f'{url}',
                                     params={"action": "order.sold",
                                             "auth": "test_user:56a356e3d3b3e5e40ac1364b8a2b5cb42ccd6fbe:99999999999",
                                             "uid": "12345678901234567893",
                                             "id": "order_id",
                                             "city_id": "41043"}, verify=False).json()
    with step("заказ продан"):
        print(order_season_sold)
        assert order_season_sold["result"], \
            f"заказ не продан"


# 10. Отменяем заказ
def test_order_season_cancel(url):
    order_season_cancel = requests.get(url=f'{url}',
                                       params={"action": "order.cancel",
                                               "auth": "test_user:56a356e3d3b3e5e40ac1364b8a2b5cb42ccd6fbe:99999999999",
                                               "uid": "12345678901234567893",
                                               "id": "order_id",
                                               "city_id": "41043"}, verify=False).json()
    with step("заказ отменен"):
        print(order_season_cancel)
        assert order_season_cancel["result"], \
            f"заказ не отменен"

