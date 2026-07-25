from app.config import COMMON_PASSWORD_FILE


special_characters = "!@#$%^&*()-_=+[]{}|\\:;\"'<>,.?/"


keyboard_patterns = [

    "qwerty",
    "asdfgh",
    "zxcvbn",
    "poiuyt",
    "lkjhg",
    "mnbvc"

]



def load_common_passwords():

    try:

        with open(COMMON_PASSWORD_FILE, "r") as file:

            return file.read().splitlines()


    except FileNotFoundError:

        return []



def detect_repeated_pattern(password):

    for i in range(len(password) - 2):

        if password[i] == password[i+1] == password[i+2]:

            return True


    return False



def detect_sequential_pattern(password):

    password = password.lower()


    sequences = [

        "0123456789",
        "9876543210",

        "abcdefghijklmnopqrstuvwxyz",
        "zyxwvutsrqponmlkjihgfedcba"

    ]


    for sequence in sequences:

        for i in range(len(sequence) - 2):

            part = sequence[i:i+3]


            if part in password:

                return True


    return False



def detect_keyboard_pattern(password):

    password = password.lower()


    for pattern in keyboard_patterns:

        if pattern in password:

            return True


    return False



def analyze_password(password):

    result = {}

    warnings = []

    suggestions = []


    common_passwords = load_common_passwords()



    result["length"] = len(password)


    result["has_upper"] = any(
        char.isupper()
        for char in password
    )


    result["has_lower"] = any(
        char.islower()
        for char in password
    )


    result["has_digit"] = any(
        char.isdigit()
        for char in password
    )


    result["has_special"] = any(
        char in special_characters
        for char in password
    )



    is_common_password = False

    has_repeated_pattern = False

    has_sequential_pattern = False

    has_keyboard_pattern = False



    if result["length"] < 8:

        warnings.append(
            "Password length is too short"
        )

        suggestions.append(
            "Use at least 8 characters"
        )



    if not result["has_upper"]:

        warnings.append(
            "No uppercase letters detected"
        )

        suggestions.append(
            "Add uppercase letters"
        )


    if not result["has_lower"]:

        warnings.append(
            "No lowercase letters detected"
        )

        suggestions.append(
            "Add lowercase letters"
        )


    if not result["has_digit"]:

        warnings.append(
            "No numbers detected"
        )

        suggestions.append(
            "Add numbers"
        )


    if not result["has_special"]:

        warnings.append(
            "No special characters detected"
        )

        suggestions.append(
            "Add special characters"
        )



    if password.lower() in common_passwords:

        is_common_password = True

        warnings.append(
            "Password is found in common password database"
        )

        suggestions.append(
            "Avoid using commonly used passwords"
        )



    if detect_repeated_pattern(password):

        has_repeated_pattern = True

        warnings.append(
            "Repeated character pattern detected"
        )

        suggestions.append(
            "Avoid repeating characters"
        )



    if detect_sequential_pattern(password):

        has_sequential_pattern = True

        warnings.append(
            "Sequential pattern detected"
        )

        suggestions.append(
            "Avoid predictable sequences like 123 or abc"
        )



    if detect_keyboard_pattern(password):

        has_keyboard_pattern = True

        warnings.append(
            "Keyboard pattern detected"
        )

        suggestions.append(
            "Avoid keyboard patterns like qwerty or asdf"
        )



    result["is_common_password"] = is_common_password

    result["has_repeated_pattern"] = has_repeated_pattern

    result["has_sequential_pattern"] = has_sequential_pattern

    result["has_keyboard_pattern"] = has_keyboard_pattern


    result["warnings"] = warnings

    result["suggestions"] = suggestions


    return result
