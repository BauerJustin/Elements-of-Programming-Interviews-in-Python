# code
def plus_one(A):
    A[-1] += 1
    for i in reversed(range(len(A))):
        if A[i] == 10 and i != 0:
            A[i-1] += 1
            A[i] = 0
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A


#tests 
import unittest

class SimpleTest(unittest.TestCase):
    def test(self):
        self.assertEqual(plus_one([1,2,9]), [1,3,0])
        self.assertEqual(plus_one([2,4,5]), [2,4,6])
        self.assertEqual(plus_one([9,9,9]), [1,0,0,0])

unittest.main()