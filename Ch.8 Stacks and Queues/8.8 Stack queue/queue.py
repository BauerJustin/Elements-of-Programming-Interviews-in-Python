class Queue:
    def __init__(self, capacity):
        self._enq = []
        self._deq = []

    def enqueue(self, x):
        self._enq.append(x)

    def dequeue(self):
        if not self._deq:
            while self._enq:
                self._deq.append(self._enq.pop())
        
        if not self._deq:
            raise IndexError("Queue empty")

        return self._deq.pop()