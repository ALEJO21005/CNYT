import unittest

def sumaComplejos(a=[], b=[]):

    real = a[0] + b[0]
    imaginaria = a[1] + b[1]
    return real, imaginaria

class pSumaComplejos(unittest.TestCase):
    
    def test_polar_cartesiano_1(self):
        self.assertEqual(sumaComplejos([1, 2], [3, 4]), (4, 6))
        
    def test_polar_cartesiano_2(self):
        self.assertEqual(sumaComplejos([5, -3], [-7, 4]), (-2, 1))

if __name__ =='__main__':
    unittest.main()