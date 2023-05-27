import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def enqueue(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def dequeue(self):
        return heapq.heappop(self._queue)[-1]

    def peek(self):
        return self._queue[0][-1]

    def count(self):
        return len(self._queue)


# Driver code
if __name__ == "__main__":
    # Basic functionality sample of Priority Queue

    # Creating priority queue which contains int in it
    pq = PriorityQueue()

    # Insert element 1 in pq
    pq.enqueue(1, 1)

    print("Size of pq is : ", pq.count(), " and Peek Element is : ", pq.peek())

    # Insert element 10 and -8 in pq
    pq.enqueue(10, 2)
    pq.enqueue(-8, 3)

    print("Size of pq is : ", pq.count(), " and Peek Element is : ", pq.peek())

    # Delete element from pq
    pq.dequeue()

    print("Size of pq is : ", pq.count(), " and Peek Element is : ", pq.peek())

    # Delete element from pq
    pq.dequeue()

    print("Size of pq is : ", pq.count(), " and Peek Element is : ", pq.peek())

    # Insert element 25 in pq
    pq.enqueue(25, 4)

    print("Size of pq is : ", pq.count(), " and Peek Element is : ", pq.peek())
