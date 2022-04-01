"""
    Задача: мы хотим создать список N максимальных или минимальных элементов коллекции.
"""
import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))
print('-'*20)

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPl', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65},
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
print(f'Using "Key" params:: \n{cheap=}, \n{expensive=}')
print('-'*20)
"""
    Примечание: если N не велико по сравнению с общим размером коллекции, то производительность nlargest и nsmallest
    будет великолепная! 'Под капотом' они начинают работу с конвертирования данных в упорядоченный список(как в куче).
    nlargest и nsmallest лучше всего подходят, если вы пытаетесь найти относительно небольшое кол-во элементов.
    Если вы хотите найти один! (N=1) наибольший или наименьший эл-т, то min() или max() будут быстрее.
    Так же если N сопоставимо с размером коллекции, то быстрее будут работать sorted(items)[:N] или sorted(items)[-N:]!
"""
heap = list(nums)
heapq.heapify(heap)
print(heap)
"""
    Примечание: heap[0] всегда будет наименьшим! heapq.heappop() - удаляет первый элемент и заменяет его следующим,
    сложность O(log N)!
"""
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print('-'*20)
