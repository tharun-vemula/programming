class LinkedStack:
    # Inner Node Class
    class _Node:
        __slots__ = "_element", "_next"

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def first(self):
        if self.is_empty():
            raise Exception("Queue Is Empty")
        return self._head._element

    def enqueue(self, e):
        newest = self._Node(e, None)

        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size = +1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue Is Empty")
        element = self._head._element
        self._head = self._head._next
        self._size -= 1

        if self.is_empty():
            self._tail = None
        return element
