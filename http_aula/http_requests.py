# requests é uma biblioteca que permite fazer requisições HTTP

import requests

url = "http://localhost:8080"

response = requests.get(url)

print(response.status_code)
print(response.text)