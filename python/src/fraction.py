from operations import add, subtract, multiply, divide, modulo
from ArbitraryInt import ArbitraryInt

class Fraction:
    def __init__(self, numerator, denominator):
        if not isinstance(numerator, ArbitraryInt):
            numerator = ArbitraryInt(str(numerator))
        if not isinstance(denominator, ArbitraryInt):
            denominator = ArbitraryInt(str(denominator))
        if denominator == ArbitraryInt('0'):
            raise ValueError("Denominator cannot be zero")
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()

    def simplify(self):
        gcd = self._gcd(abs(self.numerator), abs(self.denominator))
        self.numerator = divide(self.numerator, gcd)[0]
        self.denominator = divide(self.denominator, gcd)[0]

    def _gcd(self, a, b):
        while b != ArbitraryInt('0'):
            a, b = b, modulo(a, b)
        return a

    def __add__(self, other):
        common_denominator = multiply(self.denominator, other.denominator)
        numerator1 = multiply(self.numerator, other.denominator)
        numerator2 = multiply(other.numerator, self.denominator)
        result_numerator = add(numerator1, numerator2)
        return Fraction(result_numerator, common_denominator)

    def __sub__(self, other):
        common_denominator = multiply(self.denominator, other.denominator)
        numerator1 = multiply(self.numerator, other.denominator)
        numerator2 = multiply(other.numerator, self.denominator)
        result_numerator = subtract(numerator1, numerator2)
        return Fraction(result_numerator, common_denominator)

    def __mul__(self, other):
        result_numerator = multiply(self.numerator, other.numerator)
        result_denominator = multiply(self.denominator, other.denominator)
        return Fraction(result_numerator, result_denominator)

    def __str__(self):
        return f"{self.numerator} / {self.denominator}"

def add_fractions(fraction1, fraction2):
    return fraction1 + fraction2

def subtract_fractions(fraction1, fraction2):
    return fraction1 - fraction2

def multiply_fractions(fraction1, fraction2):
    return fraction1 * fraction2

def divide_fractions(fraction1, fraction2):
    if fraction2.numerator.value == '0':
        raise ZeroDivisionError("Cannot divide by zero fraction")
    new_numerator = multiply(fraction1.numerator, fraction2.denominator)
    new_denominator = multiply(fraction1.denominator, fraction2.numerator)
    return Fraction(new_numerator, new_denominator)