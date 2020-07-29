# code
def can_reach_end(A):
    game_map = [0] * len(A)

    for i in range(len(A)):
        for j in range(A[i]):
            if i+j >= len(A):
                break
            if game_map[i+j] != 1:
                game_map[i+j] = 1
                
    return 0 not in game_map

#tests 
import unittest

class SimpleTest(unittest.TestCase):
    def test(self):
        self.assertEqual(can_reach_end([3,3,1,0,2,0,1]), True)
        self.assertEqual(can_reach_end([3,2,0,0,2,0,1]), False)

unittest.main()