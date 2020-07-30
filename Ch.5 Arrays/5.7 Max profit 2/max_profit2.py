# code
def max_profit(A):
    max_profit = 0
    min_price = float('inf')
    max_price = float('-inf')
    a = [0] * len(A)

    for i, price in enumerate(A):
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
        a[i] = max_profit

    for i, price in reversed(list(enumerate(A[1:], 1))):
        max_price = max(max_price, price)
        max_profit = max(max_profit, max_price - price + a[i-1])
    
    return max_profit
    

#tests 
import unittest

class SimpleTest(unittest.TestCase):
    def test(self):
        self.assertEqual(max_profit([310,315,275,295,260,270,290,230,255,250]), 55)
        self.assertEqual(max_profit([12,11,13,9,12,8,14,13,15]), 10)

unittest.main()