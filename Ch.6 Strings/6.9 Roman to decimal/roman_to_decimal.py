#code
m = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def roman_to_decimal(s):
    n = 0
    for i in range(len(s)):
        if i != len(s)-1 and m[s[i]] < m[s[i+1]]:
            n -= m[s[i]]
        else:
            n += m[s[i]]
    return n

#tests 
import unittest

class SimpleTest(unittest.TestCase):
    def test(self):
        self.assertEqual(roman_to_decimal("LIX"), 59)
        self.assertEqual(roman_to_decimal("LVIIII"), 59)
        self.assertEqual(roman_to_decimal("XXXXXIIIIIIIII"), 59)

unittest.main()