import pytest
import requests


@pytest.fixture(scope='session')
def get_city_ids():
    response = requests.get(url='https://api.tickets.tst.yandex.net/api/agent/', params={"action": "city.list", "auth": "test_user:56a356e3d3b3e5e40ac1364b8a2b5cb42ccd6fbe:99999999999"}, verify=False).json()
    city_id = response['result'][0]['id']
    return city_id


@pytest.fixture(scope='session')
def get_id_for_specific_city_name():
    """
     # id города Большой московский цирк
    """
    response = requests.get(url='https://api.tickets.tst.yandex.net/api/agent/', params={"action": "city.list", "auth": "test_user:56a356e3d3b3e5e40ac1364b8a2b5cb42ccd6fbe:99999999999"}, verify=False).json()
    return response


@pytest.fixture(scope='session')
def url():
    test_domain = 'https://api.tickets.tst.yandex.net/api/agent/'
    return test_domain


