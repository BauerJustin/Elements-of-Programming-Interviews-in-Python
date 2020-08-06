#code
def modify(s):
    newS = ""
    for char in s:
        if char == "a":
            newS += "dd"
        elif char != "b":
            newS += char
    return newS

#tests 
import unittest

class SimpleTest(unittest.TestCase):
    def test(self):
        self.assertEqual(modify("acdbbca"), "ddcdcdd")
        self.assertEqual(modify("abac"), "ddddc")

unittest.main()