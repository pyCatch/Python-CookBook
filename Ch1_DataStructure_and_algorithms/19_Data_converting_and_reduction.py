"""
    Задача. Нужно выполнить функцию сокращения и (т.е. sum(), min(), max()), но сначала нужно отсортировать или
    отфильтровать данные.
"""
import os


# Подсчитать сумму квадратов
nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)
print(f'Sum of squares:: {s}')
print('-'*20)

# Определяем есть ли файлы в каталоге
files = os.listdir('./data')
if any(name.endswith('.py') for name in files):
    print('There be python')
else:
    print('Sorry, no python')
print('-'*20)

# Выводим кортеж как CSV
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))
print('-'*20)


# Сокращение (reduction) данных по полям в структуре данных
portfolio = [
    {'name': 'GOOG', 'shares': 50},
    {'name': 'YHOO', 'shares': 75},
    {'name': 'AOL', 'shares': 20},
    {'name': 'SCOX', 'shares': 65}
]
min_shares = min(s['shares'] for s in portfolio)
print(f'{min_shares=}')
full_min_shares = min(portfolio, key=lambda p: p['shares'])
print(f'{full_min_shares=}')
print('-'*20)
