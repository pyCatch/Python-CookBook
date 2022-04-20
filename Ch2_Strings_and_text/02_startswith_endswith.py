"""
    Задача. Нам нужно проверить начало или конец строки на присутствие некоторых текстовых шаблонов,
    таких как расширение файлов, схемы URL и т.д.
"""
from urllib.request import urlopen

filename = 'spam.txt'
check_file_extension: bool = filename.endswith('.txt')
check_is_url: bool = filename.startswith('file:')
print(f'Checking if file is txt:: {check_file_extension=}\n'
      f'Is filename a URL:: {check_is_url=}')

url = 'http://www.python.org'
check_is_url: bool = url.startswith('http:')
print(f'Checking if string is URL:: {check_is_url=}')
print('-'*20)
# Если нам необходимо проверить несколько вариантов мы можем передать кортеж
filenames = ['Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h']
print([name for name in filenames if name.endswith(('.c', '.h'))])
print(any(name.endswith('.py') for name in filenames))
print('-'*20)


def read_data(name):
    choices = ['http:', 'https:', 'ftp:']
    if name.startswith(tuple(choices)):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()


"""
    Примечание. Методы startswith() и endswith() предоставляют весьма удобный способ проверки префиксов и окончаний. 
    Такие же операции можно совершить с помощью срезов, но это будет менее элегантно!
"""
filename = 'spam.txt'
check_file_extension: bool = filename[-4:] == '.txt'
print(f'Checking with slicing if file is txt:: {check_file_extension=}')

url = 'http://www.python.org'
check_is_url: bool = url[:5] == 'http:' or url[:6] == 'https:' or url[:4] == 'ftp:'
print(f'Checking with slicing if string is URL:: {check_is_url=}')
