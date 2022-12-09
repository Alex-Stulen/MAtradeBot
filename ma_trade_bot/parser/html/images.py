from bs4 import BeautifulSoup

from . import FEATURES


def get_all_images(html_text: str):
    soap = BeautifulSoup(html_text, features=FEATURES)
    return soap.find_all('img')
