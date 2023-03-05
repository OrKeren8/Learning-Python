import heapq

grades = [32, 51, 62, 84, 957, 54, 62, 653]
print(heapq.nlargest(3, grades))

stocks = [
    {'ticker': 'appl', 'price': 201},
    {'ticker': 'goog', 'price': 800},
    {'ticker': 'f', 'price': 54},
    {'ticker': 'msft', 'price': 313},
    {'ticker': 'tuna', 'price': 68}
]

print(heapq.nsmallest(3, stocks, key=lambda stock: stock['price']))