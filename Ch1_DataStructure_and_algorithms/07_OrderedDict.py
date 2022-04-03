"""
    Примечание. OrderedDict сохраняет последовательность, в которой элементы были добавлены.
    В python3.6 dict() унаследовал эту функциональность!
"""
from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for key in d:
    print(key, d[key])
