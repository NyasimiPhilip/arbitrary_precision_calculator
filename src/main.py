from src.ArbitraryInt import ArbitraryInt
from src.operations import add, subtract, multiply, divide, power, factorial
from src.base_conversion import to_base, from_base
from src.fraction import Fraction, add_fractions, subtract_fractions, multiply_fractions, divide_fractions

def repl():
    print("Arbitrary Precision Calculator (Type 'exit' to quit)")
    while True:
        user_input = input("> ").strip()
        if user_input.lower() in {'exit', 'quit'}:
            break
        try:
            parts = user_input.split()
            if len(parts) < 2:
                print("Invalid input. Format: <operation> <num1> [<num2>]")
                continue
            op = parts[0]
            num1 = ArbitraryInt(parts[1])
            num2 = ArbitraryInt(parts[2]) if len(parts) > 2 else None

            if op == "add":
                print(add(num1, num2))
            elif op == "subtract":
                print(subtract(num1, num2))
            elif op == "multiply":
                print(multiply(num1, num2))
            elif op == "divide":
                quotient, remainder = divide(num1, num2)
                print(f"Quotient: {quotient}, Remainder: {remainder}")
            elif op == "power":
                print(power(num1, num2))
            elif op == "factorial":
                print(factorial(num1))
            elif op == "logarithm":
                print(logarithm(num1, num2))
            elif op == "to_base":
                base = int(parts[2])
                print(to_base(num1, base))
            elif op == "from_base":
                base = int(parts[2])
                print(from_base(parts[1], base))
            elif op == "add_fractions":
                num2 = ArbitraryInt(parts[3])
                denom2 = ArbitraryInt(parts[4])
                fraction1 = Fraction(num1, num2)
                fraction2 = Fraction(num2, denom2)
                print(add_fractions(fraction1, fraction2))
            elif op == "subtract_fractions":
                num2 = ArbitraryInt(parts[3])
                denom2 = ArbitraryInt(parts[4])
                fraction1 = Fraction(num1, num2)
                fraction2 = Fraction(num2, denom2)
                print(subtract_fractions(fraction1, fraction2))
            elif op == "multiply_fractions":
                num2 = ArbitraryInt(parts[3])
                denom2 = ArbitraryInt(parts[4])
                fraction1 = Fraction(num1, num2)
                fraction2 = Fraction(num2, denom2)
                print(multiply_fractions(fraction1, fraction2))
            elif op == "divide_fractions":
                num2 = ArbitraryInt(parts[3])
                denom2 = ArbitraryInt(parts[4])
                fraction1 = Fraction(num1, num2)
                fraction2 = Fraction(num2, denom2)
                print(divide_fractions(fraction1, fraction2))
            else:
                print("Unknown operation")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    repl()
