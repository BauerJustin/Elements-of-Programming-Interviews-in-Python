#code
def search(s, t):
    return t.find(s)

#tests 
import unittest

class SimpleTest(unittest.TestCase):
    def test(self):
        self.assertEqual(search("car", "Vroom, vroom in me mum's car."), 25)

unittest.main()