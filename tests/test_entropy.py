import sys
from pathlib import Path


sys.path.append(
    str(Path(__file__).resolve().parent.parent / "app")
)


from entropy import calculate_entropy, get_entropy_strength



def test_low_entropy_password():

    results = {

        "has_lower": False,

        "has_upper": False,

        "has_digit": True,

        "has_special": False

    }


    entropy = calculate_entropy(
        "123456",
        results
    )


    assert entropy < 40



def test_high_entropy_password():

    results = {

        "has_lower": True,

        "has_upper": True,

        "has_digit": True,

        "has_special": True

    }


    entropy = calculate_entropy(
        "N7@xLm92#Qp45",
        results
    )


    assert entropy > 60



def test_entropy_classification():

    assert get_entropy_strength(90) == "Very Strong"

    assert get_entropy_strength(50) == "Moderate"

    assert get_entropy_strength(20) == "Very Weak"