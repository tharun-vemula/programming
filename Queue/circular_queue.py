class CircularQueue:
    def __init__(self) -> None:
        self._size = 0
        self._front = 0
        self._last = 0
        self._maxsize = 10
        self._data = [None] * self._maxsize

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Exception("Queue is Empty")

        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is Empty")

        front_element = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % self._maxsize
        self._size -= 1
        return front_element

    def enqueue(self, e):
        if self.find_size == self._maxsize:
            self._resize(2 * len(self._data))
        self._data.append(e)
        self._last = (self._last + 1) % self._maxsize

    def find_size(self):
        if self._last >= self._front:
            return self._last - self._front
        return self._maxsize - (self._last - self._front)

    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front

        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (walk + 1) % len(old)

        self._front = 0
