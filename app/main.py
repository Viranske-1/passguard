from analyzer import analyze_password
from scorer import calculate_score, get_strength
from entropy import calculate_entropy


def main():

    password = input("Enter your password: ")

    # Analyze password
    results = analyze_password(password)

    # Calculate score
    score = calculate_score(results)

    # Get strength level
    strength = get_strength(score)

    # Calculate entropy
    entropy = calculate_entropy(password, results)


    print("\n===== PassGuard Report =====")

    print(f"Password Length: {results['length']}")

    print(f"Uppercase: {results['has_upper']}")

    print(f"Lowercase: {results['has_lower']}")

    print(f"Numbers: {results['has_digit']}")

    print(f"Special Characters: {results['has_special']}")

    print("----------------------------")

    print(f"Security Score: {score}/100")

    print(f"Strength: {strength}")

    print(f"Entropy: {entropy} bits")


if __name__ == "__main__":
    main()