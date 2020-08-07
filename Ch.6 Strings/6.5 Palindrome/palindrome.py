#code
def palindrome(s):
    i, j = 0, len(s) - 1
    while i < j:
        while not s[i].isalnum():
            i += 1
        while not s[j].isalnum():
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True

#tests 
import unittest

class SimpleTest(unittest.TestCase):
    def test(self):
        self.assertEqual(palindrome("Ray a Ray"), False)
        self.assertEqual(palindrome("A man, a plan, a canal, Panama"), True)

unittest.main()