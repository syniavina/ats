import pytest
import requests


@pytest.fixture(scope='session')
def url():
    """
    тестовый url
    """
    test_domain = 'https://api.tickets.tst.yandex.net/api/agent/'
    return test_domain


@pytest.fixture(scope='session')
def test_get_last_order_id():
    """
    id заказа, который получаем в ответ на запрос order.create и потом переиспользуем
    для запросов order.sold и order.cancel
    """
    response_last_order_id = requests.get(url='https://api.tickets.tst.yandex.net/api/agent/',
                                          params={"action": "order.list",
                                                  "auth": "test_user:56a356e3d3b3e5e40ac1364b8a2b5cb42ccd6fbe:99999999999",
                                                  "city_id": "41043"}, verify=False).json()
    print(response_last_order_id)
    last_order_id = response_last_order_id['result'][0]['id']
    return last_order_id



