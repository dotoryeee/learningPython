import os
import requests
from bs4 import BeautifulSoup

url = "https://www.iban.com/currency-codes"

def connect():
    r = requests.get(url)
    contents = r.text
    print(contents)

connect()