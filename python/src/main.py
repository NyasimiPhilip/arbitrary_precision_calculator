from ArbitraryInt import ArbitraryInt
from operations import add, subtract, multiply, divide, modulo, power, factorial, logarithm
from base_conversion import to_base, from_base
from fraction import Fraction, add_fractions, multiply_fractions

def repl():
    print("Arbitrary Precision Calculator (Type 'exit' to quit)")
    while True:
        try:
            user_input = input("> ").strip()
            if user_input.lower() in {'exit', 'quit'}:
                break
            
            # Split input by spaces and symbols
            parts = user_input.replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('÷', ' ÷ ').replace('^', ' ^ ').replace('/', ' / ').split()
            
            if len(parts) < 2:
                print("Invalid input. Format: <num1> <operation> [<num2>]")
                continue
            
            num1 = ArbitraryInt(parts[0])
            op = parts[1]
            num2 = ArbitraryInt(parts[2]) if len(parts) > 2 else None

            if op in {"add", "+"}:
                print(add(num1, num2))
            elif op in {"subtract", "-"}:
                print(subtract(num1, num2))
            elif op in {"multiply", "*"}:
                print(multiply(num1, num2))
            elif op in {"divide", "÷"}:
                quotient, remainder = divide(num1, num2)
                print(f"Quotient: {quotient}, Remainder: {remainder}")
            elif op in {"modulo", "%"}:
                print(modulo(num1, num2))
            elif op in {"power", "^"}:
                print(power(num1, num2))
            elif op == "factorial" or op == "!":
                print(factorial(num1))
            elif op.startswith("log"):
                base = ArbitraryInt(op[3:])  # Extract base from log2, log10, etc.
                print(logarithm(base, num1))
            elif op == "to_base":
                base = int(parts[2])
                print(to_base(num1, base))
            elif op == "from_base":
                base = int(parts[2])
                print(from_base(parts[1], base))
            elif op in {"add_fractions", "+"}:
                num2 = ArbitraryInt(parts[3])
                denom2 = ArbitraryInt(parts[4])
                fraction1 = Fraction(num1, num2)
                fraction2 = Fraction(num2, denom2)
                print(add_fractions(fraction1, fraction2))
            elif op in {"multiply_fractions", "*"}:
                num2 = ArbitraryInt(parts[3])
                denom2 = ArbitraryInt(parts[4])
                fraction1 = Fraction(num1, num2)
                fraction2 = Fraction(num2, denom2)
                print(multiply_fractions(fraction1, fraction2))
            else:
                print("Unknown operation")
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    repl()
