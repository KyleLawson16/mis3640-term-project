import requests

page = requests.get("https://www.linkedin.com/in/kylejlawson/")
print(page.status_code) #200

print(page.content)

from bs4 import BeautifulSoup

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())
print(soup.find_all("Try Premium for free"))

# print(list(soup.children)) #formats children into a list

