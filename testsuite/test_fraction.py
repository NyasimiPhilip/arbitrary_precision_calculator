import unittest
from src.ArbitraryInt import ArbitraryInt
from src.fraction import Fraction, add_fractions, subtract_fractions, multiply_fractions, divide_fractions

class TestFraction(unittest.TestCase):

    def test_add_fractions(self):
        f1 = Fraction(ArbitraryInt('1'), ArbitraryInt('2'))
        f2 = Fraction(ArbitraryInt('1'), ArbitraryInt('3'))
        result = add_fractions(f1, f2)
        self.assertEqual(str(result.numerator), '5')
        self.assertEqual(str(result.denominator), '6')

    def test_subtract_fractions(self):
        f1 = Fraction(ArbitraryInt('1'), ArbitraryInt('2'))
        f2 = Fraction(ArbitraryInt('1'), ArbitraryInt('3'))
        result = subtract_fractions(f1, f2)
        self.assertEqual(str(result.numerator), '1')
        self.assertEqual(str(result.denominator), '6')

    def test_multiply_fractions(self):
        f1 = Fraction(ArbitraryInt('1'), ArbitraryInt('2'))
        f2 = Fraction(ArbitraryInt('1'), ArbitraryInt('3'))
        result = multiply_fractions(f1, f2)
        self.assertEqual(str(result.numerator), '1')
        self.assertEqual(str(result.denominator), '6')

    def test_divide_fractions(self):
        f1 = Fraction(ArbitraryInt('1'), ArbitraryInt('2'))
        f2 = Fraction(ArbitraryInt('1'), ArbitraryInt('3'))
        result = divide_fractions(f1, f2)
        self.assertEqual(str(result.numerator), '3')
        self.assertEqual(str(result.denominator), '2')

if __name__ == '__main__':
    unittest.main()