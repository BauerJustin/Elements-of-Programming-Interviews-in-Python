# code
def reverse(x):
    new_x = str(abs(x))
    temp_x = ""
    length = len(new_x)
    for i in range(length):
        temp_x += new_x[length-1-i]
    if x < 0:
        return -int(temp_x)
    return int(temp_x)

#tests 
import unittest

class SimpleTest(unittest.TestCase):
    def test(self):
        self.assertEqual(reverse(23), 32)
        self.assertEqual(reverse(-314), -413)
        self.assertEqual(reverse(123), 321)

unittest.main()