# code
def next_permutation(A):
    index = len(A) - 2
    while index >= 0 and A[index] >= A[index+1]:
        index -= 1
    if index == -1:
        return []

    for i in reversed(range(index+1, len(A))):
        if A[i] > A[index]:
            A[index], A[i] = A[i], A[index]
            break
    
    return A[:index+1] + list(reversed(A[index+1:]))

#tests 
import unittest

class SimpleTest(unittest.TestCase):
    def test(self):
        self.assertEqual(next_permutation([1,0,3,2]), [1,2,0,3])
        self.assertEqual(next_permutation([3,2,1,0]), [])

unittest.main()