"""
    Добавление или удаление элементов в любой из концов очереди имеет сложность O(1).
    А вот вставка или удаление в начало имеет сложность О(n)
"""

from collections import deque

print('Simple queue')
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)
q.append(5)
print(q)
print('-'*20)
print('Endless queue')
endless_queue = deque()
endless_queue.append(1)
endless_queue.append(2)
endless_queue.append(3)
print(endless_queue)
endless_queue.appendleft(4)
print(endless_queue)
print(f'Pop item: {endless_queue.pop()}')
print(endless_queue)
print(f'Pop left itme: {endless_queue.popleft()}')
print(endless_queue)
print('-'*20)

for el in endless_queue:
    print(el)
