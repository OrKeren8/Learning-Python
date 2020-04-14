stocks = {
    'goog': 434,
    'appl': 325,
    'f': 54,
    'amzn': 623,
    'msft': 549
}

min_price = min(zip(stocks.values(), stocks.keys()))
print(min_price)