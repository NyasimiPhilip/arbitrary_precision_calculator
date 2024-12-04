from src.ArbitraryInt import ArbitraryInt

def add(a: ArbitraryInt, b: ArbitraryInt) -> ArbitraryInt:
    if a.is_negative == b.is_negative:
        result = _add_positive(a.value, b.value)
        return ArbitraryInt(('-' if a.is_negative else '') + result)
    else:
        if _is_greater_or_equal(a.value, b.value):
            result = _subtract_positive(a.value, b.value)
            return ArbitraryInt(('-' if a.is_negative else '') + result)
        else:
            result = _subtract_positive(b.value, a.value)
            return ArbitraryInt(('-' if b.is_negative else '') + result)

def subtract(a: ArbitraryInt, b: ArbitraryInt) -> ArbitraryInt:
    if a.is_negative != b.is_negative:
        result = _add_positive(a.value, b.value)
        return ArbitraryInt(('-' if a.is_negative else '') + result)
    else:
        if _is_greater_or_equal(a.value, b.value):
            result = _subtract_positive(a.value, b.value)
            return ArbitraryInt(('-' if a.is_negative else '') + result)
        else:
            result = _subtract_positive(b.value, a.value)
            return ArbitraryInt(('-' if not a.is_negative else '') + result)

def multiply(a: ArbitraryInt, b: ArbitraryInt) -> ArbitraryInt:
    result = [0] * (len(a.value) + len(b.value))
    val1, val2 = a.value[::-1], b.value[::-1]
    for i in range(len(val1)):
        for j in range(len(val2)):
            result[i + j] += int(val1[i]) * int(val2[j])
            result[i + j + 1] += result[i + j] // 10
            result[i + j] %= 10
    result = ''.join(map(str, result[::-1])).lstrip('0') or '0'
    is_negative = a.is_negative != b.is_negative
    return ArbitraryInt(('-' if is_negative and result != '0' else '') + result)

def divide(a: ArbitraryInt, b: ArbitraryInt) -> (ArbitraryInt, ArbitraryInt):
    if b.value == '0':
        raise ZeroDivisionError("Cannot divide by zero")
    quotient = []
    remainder = ArbitraryInt('0')
    for digit in a.value:
        remainder = ArbitraryInt(remainder.value + digit)
        count = 0
        while _is_greater_or_equal(remainder.value, b.value):
            remainder = subtract(remainder, b)
            count += 1
        quotient.append(str(count))
    quotient = ''.join(quotient).lstrip('0') or '0'
    is_negative = a.is_negative != b.is_negative
    return (ArbitraryInt(('-' if is_negative and quotient != '0' else '') + quotient), remainder)

def power(base: ArbitraryInt, exp: ArbitraryInt) -> ArbitraryInt:
    if exp.value == '0':
        return ArbitraryInt('1')
    result = ArbitraryInt('1')
    for _ in range(int(exp.value)):
        result = multiply(result, base)
    return result

def factorial(n: ArbitraryInt) -> ArbitraryInt:
    if n.is_negative:
        raise ValueError("Cannot compute factorial of a negative number")
    result = ArbitraryInt('1')
    current = ArbitraryInt('1')
    while _is_greater_or_equal(n.value, current.value):
        result = multiply(result, current)
        current = add(current, ArbitraryInt('1'))
    return result

def _add_positive(val1: str, val2: str) -> str:
    carry = 0
    result = []
    val1, val2 = val1[::-1], val2[::-1]
    for i in range(max(len(val1), len(val2))):
        digit1 = int(val1[i]) if i < len(val1) else 0
        digit2 = int(val2[i]) if i < len(val2) else 0
        total = digit1 + digit2 + carry
        result.append(str(total % 10))
        carry = total // 10
    if carry:
        result.append(str(carry))
    return ''.join(result[::-1])

def _subtract_positive(val1: str, val2: str) -> str:
    borrow = 0
    result = []
    val1, val2 = val1[::-1], val2[::-1]
    for i in range(len(val1)):
        digit1 = int(val1[i])
        digit2 = int(val2[i]) if i < len(val2) else 0
        total = digit1 - digit2 - borrow
        if total < 0:
            total += 10
            borrow = 1
        else:
            borrow = 0
        result.append(str(total))
    return ''.join(result[::-1]).lstrip('0') or '0'

def _is_greater_or_equal(val1: str, val2: str) -> bool:
    if len(val1) != len(val2):
        return len(val1) > len(val2)
    return val1 >= val2
