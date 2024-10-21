import requests
import pprint

url1 = "https://api.github.com/"
url2 = "https://jsonplaceholder.typicode.com/posts"

params1 = {
    'q': 'html'
}
params2 = {
    'userId': 1
}

response1 = requests.get(url1, params=params1)
response1_json = response1.json()
response2 = requests.get(url2, params=params2)

print("Результат задания 1:")
print(f"Статус-код: {response1.status_code}")
print(f"JSON-формат: ")
pprint.pprint(response1_json)
print()
print("Результат задания 2:")
print(f"Статус-код: {response2.status_code}")
print(f"JSON-формат: ")
pprint.pprint(response1_json)
print()