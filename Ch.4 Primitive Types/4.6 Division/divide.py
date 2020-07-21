# code
def divide(x,y):
    count = 1
    while x != y:
        x -= y
        count += 1
    return count

#tests 
import unittest

class SimpleTest(unittest.TestCase):
    def test(self):
        self.assertEqual(divide(12,3), 4)
        self.assertEqual(divide(72,9), 8)
        self.assertEqual(divide(1050,5), 210)

unittest.main()