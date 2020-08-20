class Queue:
    def __init__(self, capacity):
        self._data = [None] * capacity
        self._head = self._tail = self._num = 0

    def enqueue(self, x):
        if self._num == len(self._data):
            self._data = (self._data[self._head:] + self._data[:self._head])
            self._head = 0
            self._tail = self._num
            self._data += [None] * (len(self._data) * 2 - len(self._data))
        self._data[self._tail] = x
        self._tail = (self._tail + 1) % len(self._data)
        self._num += 1

    def dequeue(self):
        if not self._num:
            raise IndexError('Queue empty')
        self._num -= 1
        self._head = (self._head + 1) % len(self._data)
        return self._data[self._head]

    def size(self):
        return self._num