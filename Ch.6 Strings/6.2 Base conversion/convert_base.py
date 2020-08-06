import string

#code
def convert_from_int(num, base):
    return '' if num == 0 else convert_from_int(num // base, base) + string.hexdigits[num % base].upper()

def convert_base(s, b1, b2):
    num = 0
    for i in reversed(range(len(s))):
        num += pow(b1,i) * int(s[len(s)-i-1])
    return convert_from_int(num, b2)

#tests 
import unittest

class SimpleTest(unittest.TestCase):
    def test(self):
        self.assertEqual(convert_base("1101", 2, 10), "13")
        self.assertEqual(convert_base("615", 7, 13), "1A7")


unittest.main()