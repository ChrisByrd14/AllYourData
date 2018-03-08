#!/usr/bin/env python3
"""Simple program to illustrate scraping web data and saving it to a database
"""

import requests
import sys
from book import Book
from bs4 import BeautifulSoup


URL = 'http://books.toscrape.com'

page = requests.get(URL)

if page.status_code != 200:
    print('{} status code received.\nExiting.'.format(page.status_code))
    sys.exit(1)

soup = BeautifulSoup(page.content, 'html.parser')

product_elements = soup.find_all('article', {'class': 'product_pod'})

