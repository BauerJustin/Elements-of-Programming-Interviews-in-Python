# code
def alternation(A):
    A.sort()
    newA = []
    for i in range(len(A)//2):
        newA.append(A[i])
        newA.append(A[len(A)-i-1])
    return newA

#tests 
import unittest

class SimpleTest(unittest.TestCase):
    def test(self):
        self.assertEqual(alternation([1,2,3,4,5,6,7,8,9,10]), [1,10,2,9,3,8,4,7,5,6])
        self.assertEqual(alternation([10,9,8,7,6,5,4,3,2,1]), [1,10,2,9,3,8,4,7,5,6])

unittest.main()