"""
    Задача. Мы хотим создать словарь, который будет подмножеством другого словаря.
"""

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# Создать словарь всех акций с ценами больше 200
prices_more200 = {key: value for key, value in prices.items() if value > 200}
print(f'More 200:: {prices_more200}')

# Создать словарь акций технологичных компаний
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
prices_tech_companies = {key: value for key, value in prices.items() if key in tech_names}
print(f'Tech companies:: {prices_tech_companies}')

# Второй вариант более медленный
prices_tech_companies_v2 = {key: prices[key] for key in prices.keys() & tech_names}
print(f'Tech companies (slow version):: {prices_tech_companies_v2}')
