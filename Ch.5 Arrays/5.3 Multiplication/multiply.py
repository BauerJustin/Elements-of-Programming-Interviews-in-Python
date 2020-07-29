# code
def multiply(A, B):
    sign = 1
    if ((A[0] < 0 and B[0] >= 0) or (A[0] >= 0 and B[0] < 0)):
        sign = -1
    A[0], B[0]= abs(A[0]), abs(B[0])

    result = [0] * (len(A)+len(B))

    for i in reversed(range((len(A)))):
        for j in reversed(range((len(B)))):
            result[i + j + 1] += A[i] * B[j]
            result[i + j] += result[i + j + 1] // 10 
            result[i + j + 1] %= 10

    return [sign*result[0]] + result[1:]


#tests 
import unittest

class SimpleTest(unittest.TestCase):
    def test(self):
        self.assertEqual(multiply([1,9,3,7,0,7,7,2,1],[-7,6,1,8,3,8,2,5,7,2,8,7]), [-1,4,7,5,7,3,9,5,2,5,8,9,6,7,6,4,1,2,9,2,7])


unittest.main()