"""
    Задача. Мы хотим найти текст, используя те же маски, которые обычно применяются в оболочках Unix
    (например, *.py, Dat[0-9]*.csv и т.д.).
    Решение. Модуль fnmatch предоставляет две функции: fnmatch() и fnmatchcase(), которые можно использовать для
    такого поиска.
"""
from fnmatch import fnmatch, fnmatchcase

print(fnmatch('foo.txt', '*.txt'))
print(fnmatch('foo.txt', '?oo.txt'))
print(fnmatch('Dat45.csv', 'Dat[0-9]*'))

names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
print([name for name in names if fnmatch(name, 'Dat*.csv')])

"""
     Примечание. По умолчанию fnmatch() использует те же чувствительные к регистру правила, что и файловая система 
     текущей операционной системы:
     On OS X (Mac)
     fnmatch('foo.txt', '*.TXT') -> False
     On Windows
     fnmatch('foo.txt', '*.TXT') -> True
     Если это различие важно, то необходимо использовать fnmatchcase()
"""
print(fnmatchcase('foo.txt', '*.TXT'))

"""
    Примечание. Возможно использование этих функций на строках при обработке данных, или на строках,
    не являющихся именами файлов.
"""
addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 N GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY'
]
print([addr for addr in addresses if fnmatchcase(addr, '* ST')])
print([addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] * CLARK*')])

