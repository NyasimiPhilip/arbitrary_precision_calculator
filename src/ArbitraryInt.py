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
