import requests
import pprint

url1 = "https://api.github.com/"

params1 = {
    'q': 'html'
}

response1 = requests.get(url1, params=params1)
response1_json = response1.json()

print(f"Статус-код задания 1: {response1.status_code}")
print(f"JSON-формат задания 1: ")
pprint.pprint(response1_json)
print()

