# code
def partition(A, index):
    pivot = A[index]
    smallest = 0
    largest = len(A) - 1

    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[smallest] = A[smallest], A[i]
            smallest += 1

    for i in reversed(range(len(A))):
        if A[i] > pivot:
            A[i], A[largest] = A[largest], A[i]
            largest -= 1
    
    return A


#tests 
import unittest

class SimpleTest(unittest.TestCase):
    def test(self):
        self.assertEqual(partition([0,1,2,0,2,1,1], 1), [0,0,1,1,1,2,2])
        self.assertEqual(partition([0,1,2,0,2,1,1], 5), [0,0,1,1,1,2,2])
        self.assertEqual(partition([0,1,2,0,2,1,1], 6), [0,0,1,1,1,2,2])

unittest.main()