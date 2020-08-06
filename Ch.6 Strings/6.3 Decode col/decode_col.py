#code
let = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def decode_col(s):
    result = 0
    for i in reversed(range(len(s))):
        result += pow(26,i) * (let.index(s[i])+1)
    return result

#tests 
import unittest

class SimpleTest(unittest.TestCase):
    def test(self):
        self.assertEqual(decode_col("A"), 1)
        self.assertEqual(decode_col("D"), 4)
        self.assertEqual(decode_col("AA"),27)
        self.assertEqual(decode_col("ZZ"), 702)


unittest.main()