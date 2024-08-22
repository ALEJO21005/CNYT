import unittest

def dividirComplejos(a, b):

    real = (a[0]*b[0] + a[1]*b[1]) / (b[0]**2 + b[1]**2)
    imaginaria = (a[1]*b[0] - a[0]*b[1]) / (b[0]**2 + b[1]**2)
    return real, imaginaria


class pDivisionComplejos(unittest.TestCase):

    def test_dividir_complejos_1(self):
        self.assertEqual(dividirComplejos([3,4],[1,2]), (2.2,-0.4))

    def test_dividir_complejos_2(self):
        self.assertEqual(dividirComplejos([-3,1],[1,3]), (0.0,1.0))
        
if __name__ == "__main__":
    unittest.main()