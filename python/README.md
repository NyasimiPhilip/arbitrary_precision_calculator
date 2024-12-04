# Arbitrary Precision Calculator

This project is an arbitrary precision calculator implemented in Python. It supports operations on large integers, fractions, and base conversions without relying on any external libraries for core functionality. The calculator is wrapped in a REPL (Read-Eval-Print Loop) for interactive use.

## Features

- **Arbitrary Precision Integer Operations**:
  - Addition (`add`, `+`)
  - Subtraction (`subtract`, `-`)
  - Multiplication (`multiply`, `*`)
  - Division (and remainder) (`divide`, `÷`)
  - Modulo (`modulo`, `%`)
  - Exponentiation (`power`, `^`)
  - Factorial (`factorial`, `!`)

- **Fraction Operations**:
  - Addition (`add_fractions`, `+`)
  - Multiplication (`multiply_fractions`, `*`)

- **Base Conversion**:
  - Convert numbers between different bases (2 to 36).

- **Logarithms**:
  - Calculate logarithms with arbitrary bases.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/arbitrary-precision-calculator.git
   cd arbitrary-precision-calculator
   ```

2. **Ensure you have Python 3.x installed**.

3. **Install any required dependencies** (if any).

## Usage

Run the calculator in interactive mode:
`python src/main.py`    

### Interactive Commands

- `1234567890123456789 + 9876543210987654321`: Adds two numbers.
- `99999999999999999999 - 88888888888888888888`: Subtracts the second number from the first.
- `123456789 * 987654321`: Multiplies two numbers.
- `1000000000000000 ÷ 3`: Divides the first number by the second, showing quotient and remainder.
- `2^100`: Raises the first number to the power of the second.
- `50!`: Computes the factorial of a number.
- `to_base <num> <base>`: Converts a number to the specified base.
- `from_base <num> <base>`: Converts a number from the specified base to base 10.
- `1/3 + 1/4`: Adds two fractions.
- `2/5 * 3/7`: Multiplies two fractions.
- `log2(1024)`: Calculates the logarithm of a number with base 2.

## Testing

To ensure the correctness of the implementation, run the test cases provided in the `testsuite` directory.

### Running Tests

Navigate to the `testsuite` directory and execute the following command:
`python -m unittest discover`

This will automatically discover and run all the test cases.

## Project Structure

- `src/ArbitraryInt.py`: Defines the `ArbitraryInt` class for handling large integers.
- `src/operations.py`: Implements arithmetic operations for `ArbitraryInt`.
- `src/base_conversion.py`: Handles conversion of numbers between different bases.
- `src/fraction.py`: Implements operations on fractions.
- `src/main.py`: Contains the REPL for interactive use.
- `testsuite/`: Contains unit tests for all components.

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes.
4. Push to your branch.
5. Create a pull request.

## License

This project is licensed under the MIT License.