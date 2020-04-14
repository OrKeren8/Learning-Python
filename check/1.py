# import requests
# from bs4 import BeautifulSoup
#
#
# def trade_spider(max_pages):
#     page = 1
#     while page <= max_pages:
#         url = 'https://buckysroom.org/trade/search.php?page=' + str(page)
#         source_code = requests.get(url)
#         plain_text = source_code.text
#         soup = BeautifulSoup(plain_text, 'lxml')
#         for link in soup.findAll('a', {'class': 'item-name'}):
#             href = link.get('href')
#             print(href)
#         page += 1
#
# trade_spider(1)

n = 0.005
sum = 1
for i in range(10000):
    sum *= 1 - i * n
    if(1 - sum) > 0.95:
        print(i)
        break
