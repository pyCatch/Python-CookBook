"""
    Задача: мы хотим хранить ограниченную историю из нескольких последних элементов, полученных в ходе итерации
    или какого то другого процесса обработки данных.
    Код будет производить простое сопоставление текста с последовательностью строк, а при совпадении выдает
    совпавшие строки вместе с N предыдущими строками
"""
from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


if __name__ == '__main__':
    with open('./data/python_text.txt') as f:
        for line, prev_lines in search(f, 'Python', 5):
            for pline in prev_lines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)
