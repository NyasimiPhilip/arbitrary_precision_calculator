class ArbitraryInt:
    def __init__(self, value: str):
        self.is_negative = value.startswith('-')
        self.value = value.lstrip('-')  # Store number as a string
        if not self.value.isdigit():
            raise ValueError("Invalid number")
        self.value = self.value.lstrip('0') or '0'  # Normalize leading zeroes

    def __repr__(self):
        return ('-' if self.is_negative and self.value != '0' else '') + self.value

    def __abs__(self):
        return ArbitraryInt(self.value)

    def __eq__(self, other):
        if not isinstance(other, ArbitraryInt):
            return False
        return self.is_negative == other.is_negative and self.value == other.value

    def __lt__(self, other):
        if not isinstance(other, ArbitraryInt):
            return NotImplemented
        if self.is_negative != other.is_negative:
            return self.is_negative
        if self.is_negative:
            return self.value > other.value
        return self.value < other.value

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other
