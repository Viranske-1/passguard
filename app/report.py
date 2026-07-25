import json
from datetime import datetime
from pathlib import Path



REPORT_DIR = Path(__file__).resolve().parent.parent / "reports"



def generate_report(password, results, score, strength, entropy, entropy_strength):


    report = {

        "generated_at": str(datetime.now()),

        "password_analysis": {

            "length": results["length"],

            "has_uppercase": results["has_upper"],

            "has_lowercase": results["has_lower"],

            "has_numbers": results["has_digit"],

            "has_special_characters": results["has_special"],

            "common_password": results["is_common_password"],

            "repeated_pattern": results["has_repeated_pattern"],

            "sequential_pattern": results["has_sequential_pattern"],

            "keyboard_pattern": results["has_keyboard_pattern"]

        },


        "security_score": {

            "score": score,

            "strength": strength

        },


        "entropy_analysis": {

            "bits": entropy,

            "strength": entropy_strength

        },


        "warnings": results["warnings"],


        "suggestions": results["suggestions"]

    }


    REPORT_DIR.mkdir(exist_ok=True)



    filename = REPORT_DIR / "password_report.json"



    with open(filename, "w") as file:

        json.dump(
            report,
            file,
            indent=4
        )


    return filename