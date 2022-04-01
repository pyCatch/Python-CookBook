from collections import Counter
"""
    Задача. Определить какие элементы в последовательности встречаются чаще всего.
"""
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(f'{top_three=}')
print('-'*20)
"""
    Примечание. На входе объектам Counter можно скормить любую последовательность хешируемых элементов. В основе Counter 
    лежит словарь, который отображает количество вхождений элементов.
"""
print(f'{word_counts["not"]=}')
print(f'{word_counts["eyes"]=}')
print('-'*20)
"""
    Примечание. Если вы хотите увеличить счет, то можно использовать метод update()
    word_counts.update(more_words)
    Это так же можно сделать вручную, используя сложение
"""
more_words = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
for word in more_words:
    word_counts[word] += 1
print(f'{word_counts["eyes"]=}')
"""
    Примечание. Экземпляры Counter могут быть легко скомбинированы с использованием разных математических операций.
"""
a = Counter(words)
b = Counter(more_words)
print(f'{a=}')
print(f'{b=}')
c = a + b
print(f'c = a + b:: {c=}')
d = a - b
print(f'd = a - b:: {d=}')
