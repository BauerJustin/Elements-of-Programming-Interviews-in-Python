#code
def rotate(n):
    A = [[1]*(i+1) for i in range(n)]
    for i in range(n):
        for j in range(1,i):
            A[i][j] = A[i-1][j-1] + A[i-1][j]
    return A
    
#tests 
import unittest

class SimpleTest(unittest.TestCase):
    def test(self):
        self.assertEqual(rotate(5), [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]])

unittest.main()