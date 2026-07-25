from analyzer import analyze_password
from scorer import calculate_score, get_strength
from entropy import calculate_entropy, get_entropy_strength
from report import generate_report



def main():

    password = input("Enter your password: ")



    # Analyze password

    results = analyze_password(password)



    # Calculate entropy

    entropy = calculate_entropy(password, results)

    entropy_strength = get_entropy_strength(entropy)



    # Calculate security score

    score = calculate_score(results, entropy)

    strength = get_strength(score)



    print("\n===== PassGuard Report =====")



    print(f"\nPassword Length: {results['length']}")

    print(f"Uppercase: {results['has_upper']}")

    print(f"Lowercase: {results['has_lower']}")

    print(f"Numbers: {results['has_digit']}")

    print(f"Special Characters: {results['has_special']}")



    print("\n----------------------------")



    print(f"Security Score: {score}/100")

    print(f"Password Strength: {strength}")



    print(f"Entropy: {entropy} bits")

    print(f"Entropy Strength: {entropy_strength}")



    # Warnings

    if results["warnings"]:

        print("\n⚠️ Warnings:")

        for warning in results["warnings"]:

            print(f"- {warning}")



    # Suggestions

    if results["suggestions"]:

        print("\n💡 Suggestions:")

        for suggestion in results["suggestions"]:

            print(f"- {suggestion}")



    # Generate JSON report

    report_file = generate_report(
        password,
        results,
        score,
        strength,
        entropy,
        entropy_strength
    )


    print("\n📄 Report Generated:")

    print(report_file)




if __name__ == "__main__":

    main()