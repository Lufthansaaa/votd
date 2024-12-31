import requests

url = f"https://cdn.jsdelivr.net/gh/wldeh/bible-api/bibles/en-kjv/books/james/chapters/5.json"
response = requests.get(url)

print(response.text)