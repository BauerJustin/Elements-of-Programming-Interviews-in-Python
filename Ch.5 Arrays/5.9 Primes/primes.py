# code
def primes(n):
    A = [i for i in range(2,n)]
    for i in range(len(A)):
        if A[i] != 0:
            for j in range(i+A[i],len(A),A[i]):
                A[j] = 0
    return [A[i] for i in range(len(A)) if A[i] != 0]

#tests 
import unittest

class SimpleTest(unittest.TestCase):
    def test(self):
        self.assertEqual(primes(18), [2,3,5,7,11,13,17])

unittest.main()