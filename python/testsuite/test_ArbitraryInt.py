import unittest
from src.ArbitraryInt import ArbitraryInt
from src.operations import add, subtract, multiply, divide, modulo, power, factorial, logarithm
from io import StringIO
from unittest.mock import patch
from src.main import repl

class TestArbitraryInt(unittest.TestCase):

    def test_initialization(self):
        self.assertEqual(str(ArbitraryInt('123')), '123')
        self.assertEqual(str(ArbitraryInt('-123')), '-123')
        self.assertEqual(str(ArbitraryInt('000123')), '123')
        self.assertEqual(str(ArbitraryInt('-000123')), '-123')

    def test_invalid_initialization(self):
        with self.assertRaises(ValueError):
            ArbitraryInt('abc')
        with self.assertRaises(ValueError):
            ArbitraryInt('12a3')

    def test_abs(self):
        self.assertEqual(str(abs(ArbitraryInt('-123'))), '123')
        self.assertEqual(str(abs(ArbitraryInt('123'))), '123')

class TestOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(str(add(ArbitraryInt('123'), ArbitraryInt('456'))), '579')

    def test_subtract(self):
        self.assertEqual(str(subtract(ArbitraryInt('456'), ArbitraryInt('123'))), '333')

    def test_multiply(self):
        self.assertEqual(str(multiply(ArbitraryInt('123'), ArbitraryInt('456'))), '56088')

    def test_divide(self):
        quotient, remainder = divide(ArbitraryInt('123'), ArbitraryInt('10'))
        self.assertEqual(str(quotient), '12')
        self.assertEqual(str(remainder), '3')

    def test_modulo(self):
        self.assertEqual(str(modulo(ArbitraryInt('123'), ArbitraryInt('10'))), '3')

    def test_power(self):
        self.assertEqual(str(power(ArbitraryInt('2'), ArbitraryInt('10'))), '1024')

    def test_factorial(self):
        self.assertEqual(str(factorial(ArbitraryInt('5'))), '120')

    def test_logarithm(self):
        self.assertEqual(str(logarithm(ArbitraryInt('2'), ArbitraryInt('1024'))), '10')

class TestREPL(unittest.TestCase):

    def test_addition_with_whitespace(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            with patch('builtins.input', side_effect=['5 + 5', 'exit']):
                repl()
            self.assertIn('10', fake_out.getvalue())

    def test_addition_without_whitespace(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            with patch('builtins.input', side_effect=['5+5', 'exit']):
                repl()
            self.assertIn('10', fake_out.getvalue())

    def test_word_based_operations(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            with patch('builtins.input', side_effect=['5 add 5', 'exit']):
                repl()
            self.assertIn('10', fake_out.getvalue())

    def test_operator_precedence(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            with patch('builtins.input', side_effect=['5 + 5 * 2', 'exit']):
                repl()
            self.assertIn('15', fake_out.getvalue())

    def test_logarithm(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            with patch('builtins.input', side_effect=['log2(1024)', 'exit']):
                repl()
            self.assertIn('10', fake_out.getvalue())

if __name__ == '__main__':
    unittest.main()