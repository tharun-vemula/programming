class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    # Constructor for initializing the cache capacity with the given value.
    def __init__(self, cap):
        # code here
        self.capacity = cap
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    # Function to return value corresponding to the key.
    def get(self, key):
        # code here
        if key in self.cache:
            node = self.cache[key]
            self.moveToFront(node)
            return node.value
        return -1

    # Function for storing key-value pair.
    def set(self, key, value):
        # code here
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.moveToFront(node)
        else:
            if len(self.cache) == self.capacity:
                self.evictLastUsed()
            node = Node(key, value)
            self.cache[key] = node
            self.addToFront(node)

    def moveToFront(self, node):
        self.removeNode(node)
        self.addToFront(node)

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def addToFront(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def evictLastUsed(self):
        lastNode = self.tail.prev
        self.removeNode(lastNode)
        del self.cache[lastNode.key]
