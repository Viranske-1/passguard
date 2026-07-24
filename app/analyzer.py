special_characters = "!@#$%^&*()-_=+[]{}|\\:;\"'<>,.?/"


def analyze_password(password):
    result = {}

    result["length"] = len(password)

    result["has_upper"] = any(char.isupper() for char in password)

    result["has_lower"] = any(char.islower() for char in password)

    result["has_digit"] = any(char.isdigit() for char in password)

    result["has_special"] = any(
        char in special_characters for char in password
    )

    return result