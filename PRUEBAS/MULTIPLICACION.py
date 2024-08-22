import unittest 

def multiplicarComplejos(a, b):
    real = a[0] * b[0] - a[1] * b[1]
    imaginaria = a[0] * b[1] + a[1] * b[0]
    return real, imaginaria

class pMultiplicarComplejos(unittest.TestCase):

    def test_multiplicar_complejos_1(self):
        self.assertEqual(multiplicarComplejos([1, 2], [1, -2]), (5, 0))

    def test_multiplicar_complejos_2(self):
        self.assertEqual(multiplicarComplejos([3,-2],[1,2]),(7,4))

if __name__ == "__main__":
    unittest.main()
