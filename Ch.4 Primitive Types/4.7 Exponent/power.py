# code
def power(x,y):
    result = x
    for i in range(y-1):
        result *= x
    return result

#tests 
import unittest

class SimpleTest(unittest.TestCase):
    def test(self):
        self.assertEqual(power(2,3), 8)
        self.assertEqual(power(10,10), 10000000000)
        self.assertEqual(power(2.5,4), 39.0625)

unittest.main()