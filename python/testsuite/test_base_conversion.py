import unittest
from src.ArbitraryInt import ArbitraryInt
from src.base_conversion import to_base, from_base

class TestBaseConversion(unittest.TestCase):

    def test_to_base(self):
        self.assertEqual(to_base(ArbitraryInt('255'), 16), 'FF')
        self.assertEqual(to_base(ArbitraryInt('10'), 2), '1010')

    def test_from_base(self):
        self.assertEqual(str(from_base('FF', 16)), '255')
        self.assertEqual(str(from_base('1010', 2)), '10')

if __name__ == '__main__':
    unittest.main()