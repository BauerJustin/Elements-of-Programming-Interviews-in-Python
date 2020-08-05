#code
def spiral_order(A):
    newA = []
    for i in range((len(A)+1)//2):
        if i == len(A) - i - 1:
            newA.append(A[i][i])
            return newA
        newA.extend(A[i][i:-1-i])
        newA.extend(list(zip(*A))[-1-i][i:-1-i])
        newA.extend(A[-1-i][-1-i:i:-1])
        newA.extend(list(zip(*A))[i][-1-i:i:-1])
    return newA
    
#tests 
import unittest

class SimpleTest(unittest.TestCase):
    def test(self):
        self.assertEqual(spiral_order([
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]
        ), [1,2,3,6,9,8,7,4,5])
        self.assertEqual(spiral_order([
            [1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,14,15,16]
        ]
        ), [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10])

unittest.main()