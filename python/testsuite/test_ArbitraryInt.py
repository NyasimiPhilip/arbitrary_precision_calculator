import unittest
from src.ArbitraryInt import ArbitraryInt

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

if __name__ == '__main__':
    unittest.main()