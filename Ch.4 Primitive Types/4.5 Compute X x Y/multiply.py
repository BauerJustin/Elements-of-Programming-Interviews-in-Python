# code
def multiply(x,y):
    sum = 0
    while x:
        if x & 1:
            sum = add(sum, y)
        x >>= 1
        y <<= 1

    return sum

def add(a,b):
    sum = 0
    carryin = 0
    k = 1
    temp_a = a
    temp_b = b
    while temp_a or temp_b:
        ak = a & k
        bk = b & k
        carryout = (ak & bk) | (ak & carryin) | (bk & carryin)
        sum |= ak ^ bk ^ carryin
        carryin = carryout << 1
        k <<= 1
        temp_a >>= 1
        temp_b >>= 1

    return sum | carryin

#tests 
import unittest

class SimpleTest(unittest.TestCase):
    def test(self):
        self.assertEqual(multiply(3,4), 12)
        self.assertEqual(multiply(8,9), 72)

unittest.main()