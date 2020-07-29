# code
def max_profit(A):
    max = 0
    for i in range(len(A)):
        for j in range(i, len(A)):
            if A[j] - A[i] > max:
                max = A[j] - A[i]
    return max

#tests 
import unittest

class SimpleTest(unittest.TestCase):
    def test(self):
        self.assertEqual(max_profit([310,315,275,295,260,270,290,230,255,250]), 30)

unittest.main()