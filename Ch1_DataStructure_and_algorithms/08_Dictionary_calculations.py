"""
    Задача: Мы хотим проводить различные вычисления (поиск min или max, сортировку) на словаре с данными.
"""
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75,
}
min_price = min(zip(prices.values(), prices.keys()))
print(f'{min_price=}')
max_price = max(zip(prices.values(), prices.keys()))
print(f'{max_price=}')
# zip() создаёт итератор по которому можно пройтись только 1 раз!
prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names))    # Ok
# print(max(prices_and_names))    # Второй вызов ValueError: max() arg is an empty sequence
print('-'*20)
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(f'Sorted: {prices_sorted=}')
print('-'*20)
# key будет применен если значения будут совпадать
short_prices = {'AAA': 100, 'ZZZ': 100}
print(f'MIN: {min(zip(short_prices.values(), short_prices.keys()))}')
print(f'MAX: {max(zip(short_prices.values(), short_prices.keys()))}')
