print("Start scraping read application")

import requests
from bs4 import BeautifulSoup

pagina = requests.get("https://coinmarketcap.com")

allhtml = BeautifulSoup(pagina.content, 'html.parser')
table = allhtml.find('table')

print(table.prettify())