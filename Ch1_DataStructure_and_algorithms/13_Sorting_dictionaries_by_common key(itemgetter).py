"""
    Задача. Есть список словарей и мы хотим отсортировать записи согласно одному или более значений.
"""
from operator import itemgetter

rows_from_db = [
    {'fname': 'Brian', 'lname': 'Jones', 'uuid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uuid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uuid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uuid': 1004},
]

# Можно упорядочить элементы списка по общему ключю для всех словарей
rows_by_name = sorted(rows_from_db, key=itemgetter('fname'))
rows_by_uuid = sorted(rows_from_db, key=itemgetter('uuid'))

print(f'Сортировка по ключу "fname":\n {rows_by_name}')
print(f'Сортировка по ключу "uuid":\n {rows_by_uuid}')
print('-'*20)

# Можно использовать несколько параметров
rows_by_flname = sorted(rows_from_db, key=itemgetter('lname', 'fname'))
print(f'Сортировка по ключам "fname" и "lname":\n {rows_by_flname}')
print('-'*20)

"""
    Примечание. Функция sorted() принимает именованный аргумент key, который должен быть вызываемым объектом.
    Функция itemgetter() создаёт такой объект:
    itemgetter('uuid') -> operator.itemgetter('uuid').
    Этот объект так же должен принимать один аргумент из rows и возвращать значение, которое будет использоваться для
    сортировки: itemgetter('uuid')(rows_from_db[0]) -> 1003
    Функциональность itemgetter() может быть заменена lambda-функцией. Это решение хорошее но работает медленнее!
    Так же itemgetter() может быть применен и к другим функциям, например min() max()
"""

rows_by_fname = sorted(rows_from_db, key=lambda r: r['fname'])
rows_by_lfname = sorted(rows_from_db, key=lambda r: (r['lname'], r['fname']))
print(f'Сортировка по ключу "fname" с помощью lambda-выражения:\n {rows_by_fname}')
print(f'Сортировка по ключам "lname" и "fname"  с помощью lambda-выражения:\n {rows_by_lfname}')
print('-'*20)

min_uuid = min(rows_from_db, key=itemgetter('uuid'))
max_uuid = max(rows_from_db, key=itemgetter('uuid'))
print(f'Поиск записи с минимальным значение поля "uuid":\n {min_uuid}')
print(f'Поиск записи с максимальным значение поля "uuid":\n {max_uuid}')
