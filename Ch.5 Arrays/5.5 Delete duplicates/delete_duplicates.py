# code
def delete_duplicates(A):
    index = 1
    for i in range(1, len(A)):
        if A[index-1] != A[i]:
            A[index] = A[i]
            index += 1
    return A[:index] + [0]*(len(A)-index)

#tests 
import unittest

class SimpleTest(unittest.TestCase):
    def test(self):
        self.assertEqual(delete_duplicates([2,3,5,5,7,11,11,11,13]), [2,3,5,7,11,13,0,0,0])

unittest.main()