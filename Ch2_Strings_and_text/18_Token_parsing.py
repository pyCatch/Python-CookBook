"""
    Задача. У нас есть строка, которую мы хотим распарсить в поток токенов слева направо.
    text = 'foo = 23 + 42 * 10'
    Решение. Чтобы токенизировать строку, нам нужно нечто большее чем простой поиск по шаблонам. Также нам нужен способ
    определить тип шаблона. Например, мы захотим превратить строку в последовательность пар
"""
import re
from collections import namedtuple
from collections.abc import Generator
from re import Pattern

text = 'foo = 23 + 42 * 10'
tokens = [('NAME', 'foo'), ('EQ', '='), ('NUM', '23'), ('PLUS', '+'), ('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]
# Первым шагом мы должны определить все возможное токены, включая пробелы
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))

"""
    Примечание. В этих шаблонах используется условие ?P<TOKEN_NAME>, необходимое для присваивания имени шаблону.
    Далее, для токенизации мы, мы используем малоизвестный метод шаблонных объектов scanner(). Он создаст объект 
    сканера, в котором повторно вызывается шаг match() для предоставленного текста, выполняя один поиск совпадений 
    за раз. 
"""

scanner = master_pat.scanner('foo = 42')
m = scanner.match()
print(m)
print((m.lastgroup, m.group()))
m = scanner.match()
print(m)
print((m.lastgroup, m.group()))
m = scanner.match()
print(m)
print((m.lastgroup, m.group()))
m = scanner.match()
print(m)
print((m.lastgroup, m.group()))
m = scanner.match()
print(m)
print((m.lastgroup, m.group()))
m = scanner.match()
print(m)
print('-'*20)

# Example
Token = namedtuple('Token', ['type', 'value'])


def generator_tokens(pattern: Pattern[str], text: str) -> Generator:
    scanner = pattern.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())


for tok in generator_tokens(master_pat, 'foo = 42'):
    print(tok)
print('-'*20)
# Отфильтруем ненужные элементы
tokens = (tok for tok in generator_tokens(master_pat, text) if tok.type != 'WS')
for t in tokens:
    print(t)
print('-'*20)
"""
    Важно! Определение токена пробела 'WS' необходимо! Так как если встретиться текст, для которого нельзя найти 
    совпадение сканирование остановиться!
    Порядок токенов в главном регулярном выражении также важен. При поиске совпадений регулярное выражение пытается 
    отыскать совпадение с шаблоном в заданном порядке. Поэтому если шаблон окажется подстрокой более длинного шаблона,
    мы должны убедится, что более длинный шаблон вписан в выражение первым! 
"""
LT = r'(?P<LT><)'
LE = r'(?P<LT><=)'
EQ = r'(?P<LT>=)'
# master_pat = re.compile('|'.join([LE, LT, EQ]))     # Ok
# master_pat = re.compile('|'.join([LT, LE, EQ]))     # Wrong!
"""
    Примечание. Второй шаблон неправильный, потому что он не будет искать совпадение по '<='
"""

PRINT = r'(?P<PRINT>print)'
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
master_pattern = re.compile('|'.join([PRINT, NAME]))
for tok in generator_tokens(master_pattern, 'printer'):
    print(tok)
