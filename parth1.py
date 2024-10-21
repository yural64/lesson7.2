import requests
import pprint # удобна для вывода словарей

# Создаем переменную, куда будут сохраняться результаты запроса
response = requests.get("https://api.github.com/")
# print(response.status_code)
# if response.ok:
#     print("Запрос успешно выполнен")
# else:
#     print("Произошла ошибка")

print(response.text) # выводит код страницы
# print(response.content) # инфа выводится в виде байтов (b'<!....)

response_json = response.json()
pprint.pprint(response_json) # вывод информации в формате json