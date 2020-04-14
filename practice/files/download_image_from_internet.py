import random
import urllib.request #a modul for requesting a web


def download_web_image(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)

download_web_image('https://images.newscientist.com/wp-content/uploads/2019/04/08111018/screenshot-2019-04-08-10.24.34.jpg')