import requests
import pprint

url = "https://api.github.com/"

params = {
    'q': 'html'
}

response = requests.get(url, params=params)
response_json = response.json()

print(response.status_code)
pprint.pprint(response_json)
