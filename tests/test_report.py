import sys
from pathlib import Path
import json


sys.path.append(
    str(Path(__file__).resolve().parent.parent / "app")
)


from report import generate_report



def test_report_generation(tmp_path):


    results = {

        "length": 14,

        "has_upper": True,

        "has_lower": True,

        "has_digit": True,

        "has_special": True,

        "is_common_password": False,

        "has_repeated_pattern": False,

        "has_sequential_pattern": False,

        "has_keyboard_pattern": False,

        "warnings": [],

        "suggestions": []

    }


    report_file = generate_report(

        "N7@xLm92#Qp45",

        results,

        90,

        "Very Strong",

        85.5,

        "Very Strong"

    )


    assert report_file.exists()



def test_report_contains_data(tmp_path):


    results = {

        "length": 10,

        "has_upper": True,

        "has_lower": True,

        "has_digit": True,

        "has_special": True,

        "is_common_password": False,

        "has_repeated_pattern": False,

        "has_sequential_pattern": False,

        "has_keyboard_pattern": False,

        "warnings": [],

        "suggestions": []

    }


    report_file = generate_report(

        "Test@12345",

        results,

        80,

        "Strong",

        70,

        "Strong"

    )


    with open(report_file, "r") as file:

        data = json.load(file)



    assert data["security_score"]["score"] == 80

    assert data["security_score"]["strength"] == "Strong"