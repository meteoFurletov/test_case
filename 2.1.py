class CircularBufferList:
    """
    Плюсы:
    - Простота реализации: легко понять и реализовать
      с использованием базовых операций.
    - Понятность работы с индексами

    Минусы:
    - Изменение размера буфера требует дополнительных операций.
    - Высокая временная сложность для операций добавления и удаления в начало списка: O(n)
    """

    def __init__(self, capacity):
        self.buffer = [None] * capacity
        self.capacity = capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def enqueue(self, item):
        if self.size == self.capacity:
            raise Exception("Буфер заполнен")
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise Exception("Буфер пуст")
        item = self.buffer[self.head]
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return item

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity
