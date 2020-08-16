class Stack:    
    def __init__(self):    
        self._cached_max = []

    def empty(self):
        return len(self._cached_max) == 0

    def max(self):
        if self.empty():
            raise IndexError('max(): empty stack')
        return self._cached_max[-1]

    def pop(self):
        if self.empty():
            raise IndexError('pop(): empty stack')
        return self._cached_max.pop()

    def push(self, n):
        self._cached_max.append(n if self.empty() else max(n, self.max()))
    