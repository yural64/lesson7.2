import requests

url = "https://api.github.com/"

params = {
    'q': 'html'
}

response = requests.get(url, params=params)
