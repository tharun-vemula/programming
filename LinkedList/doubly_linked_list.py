class DoublyLinkedList:
    class _Node:
        __slots__ = "_element", "_prev", "_next"

        def __init__(self, element, prev, next) -> None:
            self._element = element
            self._next = next
            self._prev = prev

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer.prev = self._header
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def insert(self, e, predecessor, successor):
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def delete(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        element = node._element
        node._element = node._prev = node._next = None
        self._size -= 1
        return element
