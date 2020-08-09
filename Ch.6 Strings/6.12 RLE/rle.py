#code
def decoding(s):
    newS = ""
    for i in range(0,len(s),2):
        newS += int(s[i]) * s[i+1]
    return newS

def encoding(s):
    newS = ""
    count = 1
    for i in range(1,len(s)+1):
        if i == len(s) or s[i] != s[i-1]:
            newS += str(count) + s[i-1]
            count = 1
        else:
            count += 1
    return newS

#tests 
import unittest

class SimpleTest(unittest.TestCase):
    def test(self):
        self.assertEqual(encoding("aaaabcccaa"), "4a1b3c2a")
        self.assertEqual(decoding("4a1b3c2a"), "aaaabcccaa")
        self.assertEqual(encoding("eeeffffee"), "3e4f2e")
        self.assertEqual(decoding("3e4f2e"), "eeeffffee")

unittest.main()