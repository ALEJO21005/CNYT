import math
import unittest 

def fase(a):

    fase = math.atan2(a[1],a[0])
    return fase 


class pCalcularModulo(unittest.TestCase):
    
    def test_fase_4(self):
        self.assertAlmostEqual(fase([0, -1]), -math.pi / 2)

    def test_fase_5(self):
        self.assertAlmostEqual(fase([1, 1]), math.pi / 4)

if __name__ == "__main__":
    unittest.main()
