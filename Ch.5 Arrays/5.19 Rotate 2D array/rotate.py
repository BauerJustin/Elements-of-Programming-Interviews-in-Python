#code
def rotate(A):
    newA = []
    for j in range(len(A)):
        tempA = []
        for i in reversed(range(len(A))):
            tempA.append(A[i][j])
        newA.append(tempA)
        print(newA)
    return newA
    
#tests 
import unittest

class SimpleTest(unittest.TestCase):
    def test(self):
        self.assertEqual(rotate([
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]
        ), [
            [7,4,1],
            [8,5,2],
            [9,6,3]
        ])
        self.assertEqual(rotate([
            [1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,14,15,16]
        ]
        ), [
            [13,9,5,1],
            [14,10,6,2],
            [15,11,7,3],
            [16,12,8,4]
        ])

unittest.main()