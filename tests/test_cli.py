import sys
from pathlib import Path


sys.path.append(
    str(Path(__file__).resolve().parent.parent / "app")
)


from cli import parse_arguments



def test_password_argument():

    sys.argv = [
        "main.py",
        "--password",
        "Test@12345"
    ]


    args = parse_arguments()


    assert args.password == "Test@12345"



def test_report_argument():

    sys.argv = [
        "main.py",
        "--password",
        "Test@12345",
        "--report"
    ]


    args = parse_arguments()


    assert args.report is True



def test_verbose_argument():

    sys.argv = [
        "main.py",
        "--password",
        "Test@12345",
        "--verbose"
    ]


    args = parse_arguments()


    assert args.verbose is True