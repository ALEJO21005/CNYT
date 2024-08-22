import unittest 

def calcularModulo(a=[]):

    modulo = (a[0]**2 + a[1]**2)**0.5
    return modulo

class pCalcularModulo(unittest.TestCase):

    def test_calcular_modulo_1(self):

        self.assertAlmostEqual(calcularModulo([3, 4]), 5.0)

    def test_calcular_modulo_2(self):
        self.assertAlmostEqual(calcularModulo([-3, -4]), 5.0)

if __name__ == "__main__":
    unittest.main()
