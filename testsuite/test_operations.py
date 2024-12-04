import unittest
from src.ArbitraryInt import ArbitraryInt
from src.operations import add, subtract, multiply, divide, power, factorial

class TestOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(str(add(ArbitraryInt('123'), ArbitraryInt('456'))), '579')
        self.assertEqual(str(add(ArbitraryInt('-123'), ArbitraryInt('123'))), '0')

    def test_subtract(self):
        self.assertEqual(str(subtract(ArbitraryInt('456'), ArbitraryInt('123'))), '333')
        self.assertEqual(str(subtract(ArbitraryInt('123'), ArbitraryInt('456'))), '-333')

    def test_multiply(self):
        self.assertEqual(str(multiply(ArbitraryInt('123'), ArbitraryInt('456'))), '56088')
        self.assertEqual(str(multiply(ArbitraryInt('-123'), ArbitraryInt('456'))), '-56088')

    def test_divide(self):
        quotient, remainder = divide(ArbitraryInt('123'), ArbitraryInt('10'))
        self.assertEqual(str(quotient), '12')
        self.assertEqual(str(remainder), '3')

    def test_power(self):
        self.assertEqual(str(power(ArbitraryInt('2'), ArbitraryInt('10'))), '1024')

    def test_factorial(self):
        self.assertEqual(str(factorial(ArbitraryInt('5'))), '120')

if __name__ == '__main__':
    unittest.main()