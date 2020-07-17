# code
def closest_int_same_bit_count(x):
    for i in range(63):
        if (((x >> i) & 1) != ((x >> (i + 1)) & 1)): 
            x ^= (1 << i) | (1 << (i + 1))
            return x

# tests 
import unittest

class SimpleTest(unittest.TestCase):
    def test(self):
        self.assertEqual(closest_int_same_bit_count(6), 5)
        self.assertEqual(closest_int_same_bit_count(92), 90)
        self.assertEqual(closest_int_same_bit_count(17), 18)

unittest.main()