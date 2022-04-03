"""
    Задача. Мы хотим отсортировать объекты одного класса, но они не поддерживают операции сравнения.
    Решение. Функция sorted() принимает аргумент key(), в котором может быть передан вызываемый объект, который будет
    возвращать некоторое значение из объектов, которое sorted() будет использовать для сравнения этих объектов.
    Пример. У нас в приложении есть последовательность экземпляров класса User и мы хотим отсортировать их по атрибуту
    user_id.
"""
from operator import attrgetter


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return f'User({self.user_id})'


users = [User(23), User(3), User(99)]
print(users)
sorted_users = sorted(users, key=lambda u: u.user_id)
print(f'Sorted users:: {sorted_users}')

# Аналогичный вариант с operator.attrgetter()
another_sorted_users = sorted(users, key=attrgetter('user_id'))
print(f'Another Sorted users:: {another_sorted_users}')
"""
    Примечание. Использование attrgetter() зачастую оказывается быстрее, а так же позволяет одновременно извлекать 
    несколько полей.
    Например. Экземпляры класса User имеют так же атрибуты first_name и last_name. В это случае можем выполнить такую 
    сортировку:
        by_name = sorted(users, key=attrgetter('last_name', 'first_name'))
"""
print('-'*20)
min_user = min(users, key=attrgetter('user_id'))
print(f'Min user_id:: {min_user}')
max_user = max(users, key=attrgetter('user_id'))
print(f'Max user_id:: {max_user}')
