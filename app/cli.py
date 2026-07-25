import argparse



def parse_arguments():

    parser = argparse.ArgumentParser(
        description="PassGuard - Password Security Analyzer"
    )


    parser.add_argument(
        "--password",
        required=True,
        help="Password to analyze"
    )


    parser.add_argument(
        "--report",
        action="store_true",
        help="Generate JSON security report"
    )


    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show detailed analysis information"
    )


    return parser.parse_args()