#code
def well_formed(s):
    temp = []
    d = {'(': ')', '{': "}", '[': ']'}
    for char in s:
        if char in d:
            temp.append(char)
        elif len(temp) < 1 or d[temp.pop()] != char:
            return False
    return len(temp) < 1

#tests 
import unittest

class SimpleTest(unittest.TestCase):
    def test(self):
        self.assertEqual(well_formed("([]){()}"), True)
        self.assertEqual(well_formed("[()[]{()()}]"), True)
        self.assertEqual(well_formed("[()[]{()()"), False)
        self.assertEqual(well_formed("{)"), False)

unittest.main()