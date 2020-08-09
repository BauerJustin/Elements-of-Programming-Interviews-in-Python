#code
def snake_string(s):
    newS = ""
    for i in range(1,len(s),4):
        newS += s[i]
    for i in range(0,len(s),2):
        newS += s[i]
    for i in range(3,len(s),4):
        newS += s[i]
    return newS

#tests 
import unittest

class SimpleTest(unittest.TestCase):
    def test(self):
        self.assertEqual(snake_string("Hello_World!"), "e_lHloWrdlo!")

unittest.main()