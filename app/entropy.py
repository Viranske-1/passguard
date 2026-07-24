import math


def calculate_entropy(password, results):

    charset_size = 0

    # Lowercase characters
    if results["has_lower"]:
        charset_size += 26

    # Uppercase characters
    if results["has_upper"]:
        charset_size += 26

    # Numbers
    if results["has_digit"]:
        charset_size += 10

    # Special characters
    if results["has_special"]:
        charset_size += 32

    if charset_size == 0:
        return 0

    entropy = len(password) * math.log2(charset_size)

    return round(entropy, 2)