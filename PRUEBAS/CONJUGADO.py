import unittest 

def conjugado(a):
    conj = (a[0], a[1]*-1)
    return conj

class pConjugado(unittest.TestCase):

    def test_conjugado_1(self):
        self.assertEqual(conjugado([3,-4]),(3,4))

    def test_conjugado_2(self):
        self.assertEqual(conjugado([4,5]),(4,-5))

if __name__ == "__main__":
    unittest.main()