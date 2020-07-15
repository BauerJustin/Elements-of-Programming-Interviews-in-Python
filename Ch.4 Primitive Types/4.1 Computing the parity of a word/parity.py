# code
def parity(word):
    num = 0
    while word > 0:
        num += word & 1
        word >>= 1
    return num % 2 != 0

# tests 
import unittest

class SimpleTest(unittest.TestCase):
    def test(self):
        self.assertEqual(parity(1101), 1)
        self.assertEqual(parity(10001000), 0)

unittest.main()