from bs4 import BeautifulSoup
from functions import get_soup
from requests import get


url = get_soup("https://tellmeurl.com/erocool/").strong.text.strip()
