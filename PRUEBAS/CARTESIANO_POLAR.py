
import math
import unittest 

def cartesianoPolar(a):

    p = (a[0]**2 + a[1]**2)**0.5
    alpha = math.atan2(a[1],a[0])
    return p, alpha

class pCartesianoPolar(unittest.TestCase):

    def test_cartesiano_polar_1(self):
        self.assertEqual(cartesianoPolar([3, 4]),(5, math.atan2(4, 3)))

    def test_cartesiano_polar_2(self):
        self.assertEqual(cartesianoPolar([-1, -1]),(2**0.5, math.atan2(-1, -1)))

if __name__ == "__main__":
    unittest.main()