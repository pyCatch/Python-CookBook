data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print(f'{name=}, {date=}')

name, shares, price, (year, month, day) = data
print(f'{name=}, {shares=}, {price=}, {year=}, {month=}, {day=}')

data_string = 'Hello'
a, b, c, d, e = data_string
print(f'String unpacking:: {a=} {b=} {c=} {d=} {e=}')

_, shares, price, _ = data
print(f'{shares=}, {price=}')
print('-'*20)


"""
    Предположим, что есть записи о пользователях, которые состоят из имени, почты и произвольного количества телефонов.
"""
record1 = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
record2 = ('Dave', 'dave@example.com')
name, email, *phone_numbers = record1
print(f'{name=} {email=} {phone_numbers=}')
name, email, *phone_numbers = record2
print(f'Without phones:: {name=} {email=} {phone_numbers=}')
print('-'*20)


"""
    Есть последовательность значений, представляющая продажи вашей компании за последние восемь кварталов.
    Мы хотим посмотреть как последний квартал соотноситься со средним значением по первым семи.
"""
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(f'{trailing=}, {current=}')


def sales_stats(sales_record: list) -> str:
    *trailing_qtrs, current_qtr = sales_record
    trailing_avg = sum(trailing_qtrs) / len(trailing_qtrs)
    return f'sales_stats:: {current_qtr=} and average={trailing_avg}'


print(sales_stats(sales_record=[10, 8, 7, 1, 9, 5, 10, 3]))
print('-'*20)

"""
    Итерирование по последовательности кортежей переменной длинны.
"""
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4)
]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)
print('-'*20)

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(f'String handling:: {uname=}, {homedir=}, {sh=}')
print('-'*20)


record = ('ACME', 50, 91.1, (18, 12, 2022))
name, *_, (*_, year) = record
print(f'Ignoring variables:: {name=}, {year=}')
