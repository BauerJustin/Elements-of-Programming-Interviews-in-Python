# code
def permutation(perm, A):
    newA = [0] * len(A)
    for i in range(len(A)):
        newA[perm[i]] = A[i]
    return newA

#tests 
import unittest

class SimpleTest(unittest.TestCase):
    def test(self):
        self.assertEqual(permutation([2,0,1,3],[1,2,3,4]), [2,3,1,4])

unittest.main()