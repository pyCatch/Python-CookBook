"""
    Задача. У нас есть код, который осуществляет доступ к элементам в списке или кортеже по позиции. Однако такой подход
    часто делает программу нечитабельной. Также вы можете захотеть уменьшить зависимость от позиции в структуре данных
    путем перехода к принципу доступа к элементам по имени.
"""
from collections import namedtuple


Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub)
print(f'Email {sub.addr} was be joined at {sub.joined}')

"""
    Примечание. Хотя экземпляр namedtuple выглядит так же как и обычный экземпляр класса, он взаимозаменяем с кортежем 
    и поддерживает обычные операции кортежей, такие как индексирование и распаковка.
"""
print(len(sub))
addr, joined = sub
print(f'Email {addr} was be joined at {joined}')


"""
    Примечание. Самый частый случай использование именованного кортежа - отвязка вашего кода от работы с позициями 
    элементов, которыми он манипулирует.   
"""


def compute_cost(record: list[tuple]) -> float:
    total_cost = 0.0
    for rec in record:
        total_cost += rec[1] * rec[2]
    return total_cost


Stock = namedtuple('Stock', ['name', 'shares', 'prices'])


def new_compute_cost(record: list[tuple]) -> float:
    total_cost = 0.0
    for rec in record:
        s = Stock(*rec)
        total_cost = s.shares * s.prices
    return total_cost
print('-'*20)

"""
    Примечание. Еще одно применение именованных кортежей - замена словаря, который требует больше места для хранения.
    Но именованные кортежи - НЕИЗМЕНЯЕМЫ!!! 
"""
s = Stock('ACME', 100, 123.45)
print(s)
try:
    s.shares = 75
except Exception as err:
    print(f'namedtuple is immutable! Error:: {err}')


"""
    Примечание. Если нам все таки нужно заменить значение, то можно использовать _replace(), которым обладают экземпляры 
    именованных кортежей. Он создаст полностью новый именованный кортеж, в котором указанные значения будут заменены.
"""
s = s._replace(shares=75)
print(s)
print('-'*20)

"""
    Примечание. Тонкость использования метода _replace() заключается в том, что он может стать удобным способом 
    наполнить значениями именованный кортеж, у которого есть опциональные или отсутствующие поля. Для этого нужно 
    создать прототип кортежа, содержащий значения по умолчанию, а потом применять _replace().
"""
Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])

# Создадим экземпляр прототипа
stock_prototype = Stock('', 0, 0.0, None, None)


def dict_to_stock(input_data: dict) -> Stock:
    """Функция для преобразования словаря в Stock"""
    return stock_prototype._replace(**input_data)


# Пример работы
a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
new_stock = dict_to_stock(a)
print(f'{new_stock=}')
b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
new_stock = dict_to_stock(b)
print(f'{new_stock=}')