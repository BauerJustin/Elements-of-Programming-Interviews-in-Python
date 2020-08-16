#code
def evaluate(expression):
    results = []
    operators = {'+': lambda x,y: x+y, '-': lambda x,y: x-y, '*': lambda x,y: x*y, '/': lambda x,y: int(x/y)}
    for item in expression.split(","):
        if item in operators:
            results.append(operators[item](results.pop(),results.pop()))
        else:
            results.append(int(item))
    return results[-1]

#tests 
import unittest

class SimpleTest(unittest.TestCase):
    def test(self):
        self.assertEqual(evaluate("3,4,+,2,*,1,+"), 15)
        self.assertEqual(evaluate("1,1,+,-2,*"), -4)
        self.assertEqual(evaluate("1729"), 1729)
        self.assertEqual(evaluate("6,-30,/"), -5)

unittest.main()