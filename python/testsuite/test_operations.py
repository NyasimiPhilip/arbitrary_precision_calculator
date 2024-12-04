import unittest
from src.ArbitraryInt import ArbitraryInt
from src.operations import add, subtract, multiply, divide, modulo, power, factorial, logarithm

class TestOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(str(add(ArbitraryInt('1234567890123456789'), ArbitraryInt('9876543210987654321'))), '11111111101111111110')

    def test_subtract(self):
        self.assertEqual(str(subtract(ArbitraryInt('99999999999999999999'), ArbitraryInt('88888888888888888888'))), '11111111111111111111')

    def test_multiply(self):
        self.assertEqual(str(multiply(ArbitraryInt('123456789'), ArbitraryInt('987654321'))), '121932631112635269')

    def test_divide(self):
        quotient, remainder = divide(ArbitraryInt('1000000000000000'), ArbitraryInt('3'))
        self.assertEqual(str(quotient), '333333333333333')
        self.assertEqual(str(remainder), '1')

    def test_modulo(self):
        self.assertEqual(str(modulo(ArbitraryInt('1000000000000000'), ArbitraryInt('3'))), '1')

    def test_power(self):
        self.assertEqual(str(power(ArbitraryInt('2'), ArbitraryInt('100'))), '1267650600228229401496703205376')

    def test_factorial(self):
        # Test a smaller factorial due to size constraints
        self.assertEqual(str(factorial(ArbitraryInt('5'))), '120')

    def test_logarithm(self):
        self.assertEqual(str(logarithm(ArbitraryInt('2'), ArbitraryInt('1024'))), '10')

if __name__ == '__main__':
    unittest.main()