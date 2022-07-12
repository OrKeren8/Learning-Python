from bs4 import BeautifulSoup
import requests
import lxml


source = requests.get("https://github.com/OrKeren8/practice_projects").text
soup = BeautifulSoup(source, 'lxml')
print(soup.prettify())