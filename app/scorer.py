def calculate_score(results, entropy):

    score = 0


    # -------------------------
    # Length Score (25)
    # -------------------------

    length = results["length"]

    if length >= 16:

        score += 25

    elif length >= 12:

        score += 20

    elif length >= 8:

        score += 15

    else:

        score += 5



    # -------------------------
    # Character Diversity (25)
    # -------------------------

    diversity_score = 0


    if results["has_upper"]:

        diversity_score += 6


    if results["has_lower"]:

        diversity_score += 6


    if results["has_digit"]:

        diversity_score += 6


    if results["has_special"]:

        diversity_score += 7


    score += diversity_score



    # -------------------------
    # Entropy Score (25)
    # -------------------------

    if entropy >= 80:

        score += 25


    elif entropy >= 60:

        score += 20


    elif entropy >= 40:

        score += 15


    else:

        score += 5



    # -------------------------
    # Security Practice Score (25)
    # -------------------------

    security_score = 25



    # Common password penalty

    if results.get("is_common_password", False):

        security_score -= 20



    # Repeated pattern penalty

    if results.get("has_repeated_pattern", False):

        security_score -= 10



    # Sequential pattern penalty

    if results.get("has_sequential_pattern", False):

        security_score -= 10



    # Keyboard pattern penalty

    if results.get("has_keyboard_pattern", False):

        security_score -= 10



    # Warning penalty

    security_score -= len(results["warnings"]) * 2



    if security_score < 0:

        security_score = 0



    score += security_score



    # Maximum score limit

    if score > 100:

        score = 100



    return score




def get_strength(score):

    if score < 30:

        return "Critical"


    elif score < 50:

        return "Weak"


    elif score < 75:

        return "Moderate"


    elif score < 90:

        return "Strong"


    else:

        return "Very Strong"