"""
    Задача: мы хотим реализовать очередь, которая сортирует элементы по заданному приоритету и всегда возвращает
    элемент с наивысшим приоритетом при каждой операции получения (удаления) элемента.
"""
import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):     # O(log N)
        heapq.heappush(self._queue, (-priority, self._index, item))
        # -priority - Отрицательно для сортировки от наибольшего к наименьшему (обычная сортировка кучи от min до max)
        self._index += 1    # Необходим для правильного порядка элементов с одинаковым приоритетом.

    def pop(self):     # O(log N)
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Item({self.name})'


if __name__ == '__main__':
    q = PriorityQueue()
    q.push(Item('foo'), 1)
    q.push(Item('bar'), 5)
    q.push(Item('spam'), 4)
    q.push(Item('grok'), 1)

    print(f'Element with max priority - {q.pop()}')
    print(f'Second use pop() - {q.pop()}')
    print(f'Element witch was added first {q.pop()}')
    print(f'Element witch was added last {q.pop()}')
    print('-'*20)
    # Примечание: элементы Item не могут быть упорядочены
    # a = Item('foo')
    # b = Item('bar')
    # a < b - traceback TypeError!
    # Для этого мы можем создать кортежи (priority, item)
    a = (1, Item('foo'))
    b = (5, Item('bar'))
    print(a < b)
    # Но если приоритеты будут равны, то будет снова traceback TypeError!
    # c = (1, Item('grok'))
    # a < c - traceback TypeError!
    # Эту проблему мы решаем добавляя index (priority, index, item). Так как index всегда будет отличаться, проблема
    # будет решена (python не будет сравнивать остальные элементы кортежа, если результат уже определен!)
    a = (1, 0, Item('foo'))
    b = (5, 1, Item('bar'))
    c = (1, 2, Item('grok'))
    print(f'a<b - {a < b}')
    print(f'a<c - {a < c}')