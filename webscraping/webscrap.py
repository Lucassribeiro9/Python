# webscraping

import requests
from bs4 import BeautifulSoup

url = 'http://localhost:8080'
response = requests.get(url)
raw_html = response.text
parsed_html = BeautifulSoup(raw_html, 'html.parser')

print(parsed_html.prettify())
if parsed_html.title.string is not None:
    print(parsed_html.title.string)
print(parsed_html.find('h1').string)
