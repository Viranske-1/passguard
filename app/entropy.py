import math



def calculate_character_pool(results):

    pool_size = 0


    # Lowercase
    if results["has_lower"]:

        pool_size += 26


    # Uppercase
    if results["has_upper"]:

        pool_size += 26


    # Numbers
    if results["has_digit"]:

        pool_size += 10


    # Special characters
    if results["has_special"]:

        pool_size += 32


    return pool_size



def calculate_entropy(password, results):

    pool_size = calculate_character_pool(results)


    if pool_size == 0:

        return 0


    entropy = len(password) * math.log2(pool_size)


    return round(entropy, 2)



def get_entropy_strength(entropy):

    if entropy < 28:

        return "Very Weak"


    elif entropy < 40:

        return "Weak"


    elif entropy < 60:

        return "Moderate"


    elif entropy < 80:

        return "Strong"


    else:

        return "Very Strong"