from urllib import request

goog_url_file = 'https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1554477836&period2=1586100236&interval=1d&events=history'


def download_stock_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split('\\n')
    dest_url = r'goog.csv'#we put r before the string to make sure the / will be contained by the text
    fx = open(dest_url, 'w')
    for line in lines:
        fx.write(line + '\n')
    fx.close()


download_stock_data(goog_url_file)

