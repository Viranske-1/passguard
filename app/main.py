from app.analyzer import analyze_password
from app.scorer import calculate_score, get_strength
from app.entropy import calculate_entropy, get_entropy_strength
from app.report import generate_report
from app.logger import logger
from app.cli import parse_arguments



def main():

    try:

        # Get command line arguments
        args = parse_arguments()

        password = args.password


        # Verbose information
        if args.verbose:

            print("[INFO] Starting password analysis")


        logger.info("Password analysis started")



        # Analyze password

        if args.verbose:

            print("[INFO] Running security checks")


        results = analyze_password(password)



        # Calculate entropy

        if args.verbose:

            print("[INFO] Calculating entropy")


        entropy = calculate_entropy(
            password,
            results
        )


        entropy_strength = get_entropy_strength(
            entropy
        )



        # Calculate score

        score = calculate_score(
            results,
            entropy
        )


        strength = get_strength(
            score
        )



        # Display report

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

            print("\nWarnings:")


            for warning in results["warnings"]:

                print(f"- {warning}")



        # Suggestions

        if results["suggestions"]:

            print("\nSuggestions:")


            for suggestion in results["suggestions"]:

                print(f"- {suggestion}")



        # Generate JSON report only with --report

        if args.report:


            if args.verbose:

                print("[INFO] Generating JSON report")


            report_file = generate_report(

                password,

                results,

                score,

                strength,

                entropy,

                entropy_strength

            )


            logger.info("Security report generated")


            print("\nReport Generated:")

            print(report_file)



    except Exception as error:


        logger.error(
            f"Application error: {error}"
        )


        print("\nAn error occurred.")

        print("Check logs/passguard.log for details.")




if __name__ == "__main__":

    main()
