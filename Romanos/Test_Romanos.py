import unittest
from DecimalRoman import decimal_to_roman
class TestDecimalToRoman (unittest.TestCase):
    def test_uno(self):
        resultado = decimal_to_roman(1)
        self.assertEqual(resultado, 'I')
    def test_dos(self):
        resultado = decimal_to_roman(2)
        self.assertEqual(resultado, 'II')
    def test_cuatro(self):
        resultado = decimal_to_roman(4)
        self.assertEqual(resultado, 'IV')
    def test_cinco(self):
        resultado = decimal_to_roman(5)
        self.assertEqual(resultado, 'V')
    def test_nueve(self):
        resultado = decimal_to_roman(9)
        self.assertEqual(resultado, 'IX')
    def test_diez(self):
        resultado = decimal_to_roman(10)
        self.assertEqual(resultado, 'X')
    def test_catorce(self):
        resultado = decimal_to_roman(14)
        self.assertEqual(resultado, 'XIV')
    def test_quince(self):
        resultado = decimal_to_roman(15)
        self.assertEqual(resultado, 'XV')
    def test_cuarenta(self):
        resultado = decimal_to_roman(20)
        self.assertEqual(resultado, 'XX')
    def test_veinticuatro(self):
        resultado = decimal_to_roman(24)
        self.assertEqual(resultado, 'XXIV')
    def test_cuarenta(self):
        resultado = decimal_to_roman(40)
        self.assertEqual(resultado, 'XL')
    def test_cinquenta(self):
        resultado = decimal_to_roman(50)
        self.assertEqual(resultado, 'L')
    def test_noventa(self):
        resultado = decimal_to_roman(90)
        self.assertEqual(resultado, 'XC')
    def test_cien(self):
        resultado = decimal_to_roman(100)
        self.assertEqual(resultado, 'C')
    def test_cuatrocientos(self):
        resultado = decimal_to_roman(400)
        self.assertEqual(resultado, 'CD')
    def test_quinientos(self):
        resultado = decimal_to_roman(500)
        self.assertEqual(resultado, 'D')
    def test_novecientos(self):
        resultado = decimal_to_roman(900)
        self.assertEqual(resultado, 'CM')
    def test_mil(self):
        resultado = decimal_to_roman(1000)
        self.assertEqual(resultado, 'M')


if __name__ == "__main__":
    unittest.main()


import unittest
from RomanDecimal import RomanToDecimal
class TestRomanToDecimal(unittest.TestCase):
    def testUno(self):
        resultado = RomanToDecimal('I')
        self.assertEqual(resultado, 1)
    def testCinco(self):
        resultado = RomanToDecimal('V')
        self.assertEqual(resultado, 5)
    def testDiez(self):
        resultado = RomanToDecimal('X')
        self.assertEqual(resultado, 10)
    def testCinquenta(self):
        resultado = RomanToDecimal('L')
        self.assertEqual(resultado, 50)
    def testCien(self):
        resultado = RomanToDecimal('C')
        self.assertSetEqual(resultado, 100)
    def testQuinientos(self):
        resultado = RomanToDecimal('D')
        self.assertEqual(resultado, 500)
    def testMil(self):
        resultado = RomanToDecimal('M')
        self.assertEqual(resultado, 1000)

if __name__ == "__main__":
    unittest.main()
