import os
from ArbitraryInt import ArbitraryInt
from operations import add, subtract, multiply, divide, modulo, power, factorial, logarithm
from base_conversion import to_base, from_base
from fraction import Fraction, add_fractions, multiply_fractions

def print_guide():
    guide = """
    **Arbitrary Precision Integer Operations**:
      - Addition (`add`, `+`)
      - Subtraction (`subtract`, `-`)
      - Multiplication (`multiply`, `*`)
      - Division (and remainder) (`divide`, `÷`, `/`)
      - Modulo (`modulo`, `%`)
      - Exponentiation (`power`, `^`)
      - Factorial (`factorial`, `!`)

    **Fraction Operations**:
      - Addition (`add_fractions`, `+`)
      - Multiplication (`multiply_fractions`, `*`)

    **Base Conversion**:
      - Convert numbers between different bases (2 to 36).

    **Logarithms**:
      - Calculate logarithms with arbitrary bases.
    """
    print(guide)

def parse_fraction(fraction_str):
    num, denom = map(ArbitraryInt, fraction_str.split('/'))
    return Fraction(num, denom)

def evaluate_expression(tokens):
    # Operator precedence
    precedence = {'+': 1, '-': 1, '*': 2, '÷': 2, '/': 2, '%': 2, '^': 3}
    operators = []
    operands = []

    def apply_operator():
        if not operators or len(operands) < 2:
            raise ValueError("Invalid expression")
        op = operators.pop()
        right = operands.pop()
        left = operands.pop()
        if op == '+':
            operands.append(add(left, right))
        elif op == '-':
            operands.append(subtract(left, right))
        elif op == '*':
            operands.append(multiply(left, right))
        elif op in {'÷', '/'}:
            quotient, remainder = divide(left, right)
            operands.append((quotient, remainder))
        elif op == '%':
            operands.append(modulo(left, right))
        elif op == '^':
            operands.append(power(left, right))

    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token.endswith('!') and token[:-1].isdigit():
            # Handle factorial directly after a number
            num = ArbitraryInt(token[:-1])
            operands.append(factorial(num))
        elif token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
            operands.append(ArbitraryInt(token))
        elif token == '!':
            if not operands:
                raise ValueError("Invalid expression")
            num = operands.pop()
            operands.append(factorial(num))
        elif token in precedence:
            while (operators and operators[-1] in precedence and
                   precedence[operators[-1]] >= precedence[token]):
                apply_operator()
            operators.append(token)
        elif token.startswith('log'):
            base = ArbitraryInt(token[3:])
            num = operands.pop()
            operands.append(logarithm(base, num))
        elif token == 'to_base':
            num = operands.pop()
            base = int(tokens[i + 1])
            operands.append(to_base(num, base))
            i += 1
        elif token == 'from_base':
            num = tokens[i + 1]
            base = int(tokens[i + 2])
            operands.append(from_base(num, base))
            i += 2
        elif token in {'add_fractions', 'multiply_fractions'}:
            if len(operands) < 2:
                raise ValueError("Invalid expression for fractions")
            right = operands.pop()
            left = operands.pop()
            if not isinstance(left, Fraction) or not isinstance(right, Fraction):
                raise ValueError("Both operands must be fractions")
            if token == 'add_fractions':
                operands.append(add_fractions(left, right))
            elif token == 'multiply_fractions':
                operands.append(multiply_fractions(left, right))
        else:
            raise ValueError(f"Invalid token: {token}")
        i += 1

    while operators:
        apply_operator()

    if len(operands) != 1:
        raise ValueError("Invalid expression")

    return operands[0]

def normalize_input(user_input):
    # Normalize input by adding spaces around operators and handling text-based operations
    replacements = {
        '+': ' + ', '-': ' - ', '*': ' * ', '÷': ' ÷ ', '/': ' / ', '^': ' ^ ',
        'add': ' + ', 'subtract': ' - ', 'multiply': ' * ', 'divide': ' ÷ ',
        'modulo': ' % ', 'power': ' ^ ', 'factorial': ' ! ', 'logarithm': ' log '
    }
    for key, value in replacements.items():
        user_input = user_input.replace(key, value)
    return user_input

def clear_screen():
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

def repl():
    print("Arbitrary Precision Calculator (Type 'exit' to quit)")
    print_guide()
    while True:
        try:
            user_input = input("> ").strip()
            if user_input.lower() in {'exit', 'quit'}:
                break
            if user_input.lower() == 'help':
                print_guide()
                continue
            if user_input.lower() == 'clear':
                clear_screen()
                continue
            
            # Normalize input
            normalized_input = normalize_input(user_input)
            
            # Split input by spaces
            parts = normalized_input.split()
            
            if len(parts) < 1:
                print("Invalid input. Format: <num1> <operation> <num2> [<operation> <num3> ...]")
                continue
            
            # Evaluate the expression
            result = evaluate_expression(parts)
            if isinstance(result, tuple):
                quotient, remainder = result
                if remainder.value == '0':
                    print(quotient)
                else:
                    print(f"{quotient} remainder {remainder}")
            elif isinstance(result, Fraction):
                print(f"{result.numerator} / {result.denominator}")
            else:
                print(result)
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    repl()
