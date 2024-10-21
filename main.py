import requests
import pprint

url1 = "https://api.github.com/"

params1 = {
    'q': 'html'
}

response1 = requests.get(url1, params=params1)
response1_json = response1.json()

print(response1.status_code)
pprint.pprint(response1_json)
