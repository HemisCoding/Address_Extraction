import requests
from bs4 import BeautifulSoup

# make a request to the website
url = "http://olympus.realpython.org/profiles/aphrodite"
page = requests.get(url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")

print(html)


