def calculate_score(results):
    score = 0

    # Length check
    if results["length"] >= 8:
        score += 20

    # Uppercase check
    if results["has_upper"]:
        score += 20

    # Lowercase check
    if results["has_lower"]:
        score += 20

    # Digit check
    if results["has_digit"]:
        score += 20

    # Special character check
    if results["has_special"]:
        score += 20

    return score


def get_strength(score):

    if score < 40:
        return "Weak"

    elif score < 80:
        return "Medium"

    else:
        return "Strong"