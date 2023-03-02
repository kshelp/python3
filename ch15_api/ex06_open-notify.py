import requests
import json

url = "http://api.open-notify.org/iss-now.json"

r = requests.get(url)
print(r.text)
'''
{"message": "success", "iss_position": {"longitude": "-155.5470", "latitude": "13.6561"}, "timestamp": 1637328033}
'''


import requests
import time

url = "http://api.open-notify.org/iss-now.json"

def ISS_Position(iss_position_api_url):
    json_to_dict = requests.get(iss_position_api_url).json()
    return json_to_dict["iss_position"]

for k in range(5):
    print(ISS_Position(url))
    time.sleep(10)  # 10초 동안 코드 실행을 일시적으로 중지한다. 
'''
{'longitude': '-152.1241', 'latitude': '9.0961'}
{'longitude': '-151.7364', 'latitude': '8.5671'}
{'longitude': '-151.3498', 'latitude': '8.0377'}
'''