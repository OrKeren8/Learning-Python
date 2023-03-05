import heapq
from operator import itemgetter


grades = [32, 51, 62, 84, 957, 54, 62, 653]
print(heapq.nlargest(3, grades))

stocks = [
    {'ticker': 'appl', 'price': '201'},
    {'ticker': 'goog', 'price': '800'},
    {'ticker': 'f',    'price': '54'},
    {'ticker': 'msft', 'price': '313'},
    {'ticker': 'tuna', 'price': '68'},
    {'ticker': 'tuna', 'price': '61'}

]

#  sort the listv by the keys of the dic
print(heapq.nsmallest(3, stocks, key=lambda stock: stock['price']))
print('-----')

for x in sorted(stocks, key=itemgetter('ticker')):
    print(x)


print('-----')
for x in sorted(stocks, key=itemgetter('ticker', 'price')):
    print(x)

