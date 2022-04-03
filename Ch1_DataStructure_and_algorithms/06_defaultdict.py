"""
    Примечание. Особенность defaultdict заключается в автоматической инициализации первого значения, так что мы можем
    сосредоточится на добавлении элементов.
"""
from collections import defaultdict


d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(3)
d['b'].append(4)
d['b'].append(5)
print(d)

d2 = defaultdict(set)
d2['a'].add(1)
d2['a'].add(2)
d2['a'].add(3)
d2['b'].add(4)
d2['b'].add(5)
print(d2)

"""
    Примечание. Конструирование таких словарей не является чем то сложным. Однако инициализация первого значения может 
    быть запутанной. Использование defaultdict приводит к наиболее чистому коду.
"""
d = {}
for key, value in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)

dd = defaultdict(list)
for key, value in pairs:
    dd[key].append(value)
