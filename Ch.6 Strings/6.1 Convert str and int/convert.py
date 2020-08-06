#code
def int_to_string(n):
    return str(n)

def string_to_int(s):
    return int(s)

#tests 
import unittest

class SimpleTest(unittest.TestCase):
    def test(self):
        self.assertEqual(string_to_int("314"), 314)
        self.assertEqual(string_to_int("-25"), -25)
        self.assertEqual(int_to_string(314), "314")
        self.assertEqual(int_to_string(-25), "-25")

unittest.main()