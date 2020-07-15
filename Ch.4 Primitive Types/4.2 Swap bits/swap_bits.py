# code
def swap_bits(number,i,j):
    if (number >> i) & 1 != (number >> j) & 1:
        number ^= (1 << i) | (1 << j)
    return number

# tests 
import unittest

class SimpleTest(unittest.TestCase):
    def test(self):
        self.assertEqual(swap_bits(73, 1, 6), 11)

unittest.main()