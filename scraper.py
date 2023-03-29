import requests
from bs4 import BeautifulSoup

# product_code = input("Podaj kod produktu:\n>> ")
product_code = "144327733"
url = f"https://www.ceneo.pl/{product_code}#tab=reviews"
response = requests.get(url)
status_code = response.status_code
content = response.text
soup = BeautifulSoup(content, "html.parser")
print(soup.prettify())