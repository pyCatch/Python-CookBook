"""
    Задача: допустим что у нас есть код, который вытаскивает определенные поля с данными из строковых записей с
    фиксированным набором полей (т.е. из файла с плоской структурой или похожего формата)
    ###### 01234567890123456789012345678901234567890'
    record = '..................100............513.25.............'
    cost = int(record[18:21] * float(record[33:39])
"""

record = '..................100............513.25.............'
SHARES = slice(18, 21)
PRICE = slice(33, 39)
cost = int(record[SHARES]) * float(record[PRICE])


# Встроенная функция slice() создает объект среза, который может быть использован везде, где применяются срезы!
items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
print(f'Common slicing:: {items[2:4]}')
print(f'Named slice:: {items[a]}')
print(f'{items[2:4] == items[a]}')
print('-'*20)
items[a] = [10, 11]
print(f'Added elements {items=}')
del items[a]
print(f'Deleted elements {items=}')
print('-'*20)
"""
    Примечание! Если есть экземпляр slice, сохраненный в переменной s, можно получить больше информации о нем, с помощью
    атрибутов s.start, s.stop, s.step!
"""
s = slice(10, 50, 2)
print(f'Slice:: {s=}')
print(f'Slice attributes:: {s.start=}, {s.stop=}, {s.step=}')
print('-'*20)
"""
    Примечание! Также можно наложить срез на последовательность определенного размера, используя его метод indices(size).
    Он вернет кортеж (start, stop, step), где все значения соответственно ограничены, чтобы вписаться в границы (дабы 
    избежать возбуждения исключений IndexError при индексировании).
"""

data_string = 'HelloWorld'
slc = slice(5, 50, 2)
print(f'Slice:: {slc=}')
print(f'New slice:: {slc.indices(len(data_string))}')
for i in range(*slc.indices(len(data_string))):
    print(f'{i=}')
    print(data_string[i])
