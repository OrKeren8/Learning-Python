import requests
from bs4 import BeautifulSoup


def sell_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://www.udemy.com/courses/development/?p=' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'lxml') #this line should take the txt of the web and make it as an object of beautifall soup
        print(soup)
        momo = soup.find('mata')
        print(momo)
        # for header in soup.findAll()
        page += 1


sell_spider(7)