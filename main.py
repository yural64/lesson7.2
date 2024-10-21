import requests
import pprint

# 1, 2 и 3 в именах переменных - номера заданий (игнорирую, что url 2 и 3 задания одинаковые)

url1 = "https://api.github.com/"
url2 = "https://jsonplaceholder.typicode.com/posts"
url3 = "https://jsonplaceholder.typicode.com/posts"

params1 = {
    'q': 'html'
}
params2 = {
    'userId': 1
}

data3 = {
    'title': 'foo', 'body': 'bar', 'userId': 1
}

response1 = requests.get(url1, params=params1)
response1_json = response1.json()

print("Результат задания 1:")
print(f"Статус-код: {response1.status_code}")
print(f"JSON-формат: ")
pprint.pprint(response1_json)
print()

response2 = requests.get(url2, params=params2)
if response2.status_code == 200:
    posts = response2.json()
    print("Результат задания 2:")
    for post in posts:
        print(post)
    else:
        print("Ошибка")
print()

response3 = requests.post(url3, data=data3)
response3_json = response3.json()

print("Результат задания 3:")
print(f"Статус-код: {response3.status_code}")
print(f"Ответ: {response3_json}")
