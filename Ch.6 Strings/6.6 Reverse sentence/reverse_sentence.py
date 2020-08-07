#code
def reverse_sentence(s):
    A = []
    for word in s.split():
        A.append(word)
    newS = ""
    for word in reversed(A):
        newS += word + " "
    return newS.rstrip()

#tests 
import unittest

class SimpleTest(unittest.TestCase):
    def test(self):
        self.assertEqual(reverse_sentence("Alice likes Bob"), "Bob likes Alice")

unittest.main()