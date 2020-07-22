# code
def palindrome(x):
    if x < 0:
        return False
    length = len(str(x))
    divisor = 10**(length-1)
    for i in range(length//2):
        if x // divisor != x % 10:
            return False
        x %= divisor
        x //= 10
        divisor //= 100         
    return True

#tests 
import unittest

class SimpleTest(unittest.TestCase):
    def test(self):
        self.assertEqual(palindrome(2147447412), True)
        self.assertEqual(palindrome(1), True)
        self.assertEqual(palindrome(333), True)
        self.assertEqual(palindrome(462325273), False)
        self.assertEqual(palindrome(12), False)
        self.assertEqual(palindrome(-1), False)
        self.assertEqual(palindrome(0), True)


unittest.main()