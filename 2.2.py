from collections import deque


class CircularBufferDeque:
    """
    Плюсы:
    - Автоматическое управление размером
    - Низкая временная сложность для операций добавления и удаления: O(1)

    Минусы:
    - При использовании deque невозможно работать с индексами, как в списках.
    """

    def __init__(self, capacity):
        self.buffer = deque(maxlen=capacity)
        self.capacity = capacity

    def enqueue(self, item):
        if len(self.buffer) == self.capacity:
            # Автоматически удаляет старый элемент при переполнении, если это необходимо.
            self.buffer.popleft()
        self.buffer.append(item)

    def dequeue(self):
        if len(self.buffer) == 0:
            raise Exception("Буфер пуст")
        return self.buffer.popleft()

    def is_empty(self):
        return len(self.buffer) == 0

    def is_full(self):
        return len(self.buffer) == self.capacity
