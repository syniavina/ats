import requests
import json
import certifi
import urllib3


# API Url
response = requests.get(url='https://api.tickets.tst.yandex.net/api/agent/', params={"action": "city.list", "auth": "test_user:56a356e3d3b3e5e40ac1364b8a2b5cb42ccd6fbe:99999999999"}, verify=False).json()
print(response)

# parse response to Json data
# dir(response)
#json_response = json.loads(response.text)
#print(json_response)

