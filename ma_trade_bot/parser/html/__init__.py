from bs4 import BeautifulSoup

FEATURES = 'html.parser'


def get_all_by_tag_name(html_text: str, tag_name: str):
    soap = BeautifulSoup(html_text, features=FEATURES)
    return soap.find_all(tag_name)
