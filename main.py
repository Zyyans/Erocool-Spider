from bs4 import BeautifulSoup

from requests import get


url = BeautifulSoup(get("https://tellmeurl.com/erocool/").text, "lxml").strong.text.strip()
