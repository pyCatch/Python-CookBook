"""
    Задача: у нас есть два словаря и мы хотим выяснить, что у нис общего (одинаковые ключи, значения и тп.)
"""
a = {
    'x': 1,
    'y': 2,
    'z': 3,
}
a1 = {
    'x': 1,
    'y': 2,
    'z': 3,
}
b = {
    'w': 10,
    'x': 11,
    'y': 2,
}

print(f'Shared keys:: {a.keys() & b.keys()}')
print(f'Different keys:: {a.keys() - a1.keys()}')
print(f'Shared pairs:: {a.items() & b.items()}')
print('-'*20)

"""
    Задача: предположим что мы хотим создать словарь, в котором некоторые ключи удалены.
"""
c = {key: a[key] for key in a.keys() - {'z', 'w'}}
print(c)
print('-'*20)
