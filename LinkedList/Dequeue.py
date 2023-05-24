from doubly_linked_list import DoublyLinkedList


class Dequeue(DoublyLinkedList):
    def first(self):
        if self.is_empty():
            raise Exception("Dequeue is Empty")
        return self._header._next._element

    def last(self):
        if self.is_empty():
            raise Exception("Dequeue is Empty")
        return self._trailer._prev._element

    def insert_front(self, e):
        self.insert(e, self._header, self._header._next)

    def insert_last(self, e):
        self.insert(e, self._trailer._prev, self._trailer)

    def delete_front(self):
        if self.is_empty():
            raise Exception("Dequeue is Empty")

        self.delete(self._header._next)

    def delete_last(self):
        if self.is_empty():
            raise Exception("Dequeue is Empty")

        self.delete(self._trailer._prev)
