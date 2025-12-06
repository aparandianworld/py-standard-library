from operator import itemgetter

# stocks, opening value, closing value
stocks = [
    ("APPL", 188.34, 202.78),
    ("MSFT", 275.80, 277.22),
    ("FB", 264.50, 266.00),
    ("GOOG", 1168.90, 1170.00),
    ("TWTR", 26.96, 27.00),
]


# sort the list by closing value in descending order
def sort_stocks(stocks):
    sorted_stocks = sorted(stocks, key=lambda item: item[2], reverse=True)
    return sorted_stocks


def sort_stocks_itemgetter(stocks):
    sorted_stocks = sorted(stocks, key=itemgetter(2), reverse=True)
    return sorted_stocks


print("stocks:", stocks)
print("sorted stocks: ", sort_stocks(stocks))
print("sorted stocks itemgetter: ", sort_stocks_itemgetter(stocks))
