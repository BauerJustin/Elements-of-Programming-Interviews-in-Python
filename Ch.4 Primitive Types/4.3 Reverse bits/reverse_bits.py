# code
def reverse_bits(x):
    return int('{:08b}'.format(x)[::-1], 2)

# tests 
import unittest

class SimpleTest(unittest.TestCase):
    def test(self):
        self.assertEqual(reverse_bits(65), 130)

unittest.main()