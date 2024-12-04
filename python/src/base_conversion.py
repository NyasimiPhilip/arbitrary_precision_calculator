from ArbitraryInt import ArbitraryInt
from operations import divide, multiply, add

def to_base(n: ArbitraryInt, base: int) -> str:
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36")
    
    # Handle negative numbers
    sign = '-' if n.is_negative else ''
    n = ArbitraryInt(n.value)  # Ensure n is positive for conversion
    n.is_negative = False
    
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    
    while n.value != '0':
        quotient, remainder = divide(n, ArbitraryInt(str(base)))
        result.append(digits[int(remainder.value)])
        n = quotient

    return sign + ''.join(result[::-1]) or '0'

def from_base(s: str, base: int) -> ArbitraryInt:
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36")
    
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    s = s.strip()
    
    # Check if number is negative
    is_negative = s.startswith('-')
    if is_negative:
        s = s[1:]
    
    result = ArbitraryInt('0')
    for char in s:
        if char.upper() not in digits[:base]:
            raise ValueError(f"Invalid character '{char}' for base {base}")
        value = digits.index(char.upper())
        result = multiply(result, ArbitraryInt(str(base)))
        result = add(result, ArbitraryInt(str(value)))
    
    return ArbitraryInt('-' + result.value if is_negative else result.value)