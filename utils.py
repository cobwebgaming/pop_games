import requests
from bs4 import BeautifulSoup

def get_wiki_page_first_paragraph(title):
    url = 'https://en.wikipedia.org/wiki/' + title
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    p = soup.findAll('p')[0]
    return p.text
        


