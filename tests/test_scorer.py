import sys
from pathlib import Path


sys.path.append(str(Path(__file__).resolve().parent.parent / "app"))


from scorer import calculate_score, get_strength


def test_calculate_score_for_a_strong_password():
    results = {
        "length": 13,
        "has_upper": True,
        "has_lower": True,
        "has_digit": True,
        "has_special": True,
        "warnings": [],
    }

    assert calculate_score(results, entropy=65) == 90


def test_get_strength():
    assert get_strength(90) == "Very Strong"
