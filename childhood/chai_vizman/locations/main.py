import requests
from bs4 import BeautifulSoup


def trade_spider(start_location, stop_location):
    url = 'https://www.google.co.il/maps/dir/' + start_location + '%E2%80%AD/' + stop_location
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'lxml')
    for link in soup.findAll('a', {"jstcache": "1041"}):
        momo = link.span
        print(momo)


trade_spider('תל אביב', 'דימונה')
