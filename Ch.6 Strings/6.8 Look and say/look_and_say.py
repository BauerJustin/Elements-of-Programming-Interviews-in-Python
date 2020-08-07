#code
def look_and_say(n):
    s = "1"
    for _ in range(1,n):
        result = []
        i = 0
        while i < len(s):
            count = 1
            while i + 1 < len(s) and s[i] == s[i+1]:
                i += 1
                count += 1
            result.append(str(count)+s[i])
            i += 1
        s = ''.join(result)
    return s

#tests 
import unittest

class SimpleTest(unittest.TestCase):
    def test(self):
        self.assertEqual(look_and_say(3), '21')
        self.assertEqual(look_and_say(6), '312211')
        self.assertEqual(look_and_say(8), '1113213211')

unittest.main()