from bs4 import BeautifulSoup
import requests
import lxml


source = requests.get("https://github.com/OrKeren8/practice_projects/pulls").text
soup = BeautifulSoup(source, 'lxml')
# print(soup.prettify())

merge_requests = soup.find('div', class_="Box mt-3 Box--responsive hx_Box--firstRowRounded0")

x = str(merge_requests)
link = merge_requests.find('Issue')
print(link)
# for link in merge_requests.find_all('a', href=True):
#     print(link)
    
# print(issue.prettify())