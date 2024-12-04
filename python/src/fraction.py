from ArbitraryInt import ArbitraryInt
from operations import add, subtract, multiply, divide, gcd

class Fraction:
    def __init__(self, numerator: ArbitraryInt, denominator: ArbitraryInt):
        if denominator.value == '0':
            raise ZeroDivisionError("Denominator cannot be zero")
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()

    def __repr__(self):
        return f"{self.numerator} / {self.denominator}"

    def simplify(self):
        gcd_value = gcd(self.numerator, self.denominator)
        self.numerator = divide(self.numerator, gcd_value)[0]
        self.denominator = divide(self.denominator, gcd_value)[0]

def add_fractions(f1: Fraction, f2: Fraction) -> Fraction:
    numerator = add(multiply(f1.numerator, f2.denominator), multiply(f2.numerator, f1.denominator))
    denominator = multiply(f1.denominator, f2.denominator)
    return Fraction(numerator, denominator)

def subtract_fractions(f1: Fraction, f2: Fraction) -> Fraction:
    numerator = subtract(multiply(f1.numerator, f2.denominator), multiply(f2.numerator, f1.denominator))
    denominator = multiply(f1.denominator, f2.denominator)
    return Fraction(numerator, denominator)

def multiply_fractions(f1: Fraction, f2: Fraction) -> Fraction:
    numerator = multiply(f1.numerator, f2.numerator)
    denominator = multiply(f1.denominator, f2.denominator)
    return Fraction(numerator, denominator)

def divide_fractions(f1: Fraction, f2: Fraction) -> Fraction:
    numerator = multiply(f1.numerator, f2.denominator)
    denominator = multiply(f1.denominator, f2.numerator)
    return Fraction(numerator, denominator)
