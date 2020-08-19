#code
def building_height(sequence):
    buildings = []
    for building in sequence:
        while buildings and building >= buildings[-1]:
            buildings.pop()
        buildings.append(building)
    return buildings

#tests 
import unittest

class SimpleTest(unittest.TestCase):
    def test(self):
        self.assertEqual(building_height([4,5,2,3,3,1]), [5,3,1])
        self.assertEqual(building_height([10,9,8,9,7,3,5,6,3]), [10,9,7,6,3])

unittest.main()