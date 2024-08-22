import math
import unittest

def polarCartesiano(a):
    a0 = a[0] * math.cos(a[1])
    a1 = a[0] * math.sin(a[1]) 
    return a0, a1

class pPolarCartesiano(unittest.TestCase):  

    def test_polar_cartesiano_1(self):
        self.assertEqual(polarCartesiano([1, math.pi / 4]), (math.cos(math.pi / 4), math.sin(math.pi / 4)))

    def test_polar_cartesiano_2(self):
        self.assertEqual(polarCartesiano([10, 2 * math.pi]), (10 * math.cos(2 * math.pi), 10 * math.sin(2 * math.pi)))

if __name__ == "__main__":
    unittest.main()
