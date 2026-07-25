import sys
from pathlib import Path


# Add app folder to Python path

sys.path.append(
    str(Path(__file__).resolve().parent.parent / "app")
)


from analyzer import analyze_password



def test_common_password_detection():

    result = analyze_password("password")


    assert result["is_common_password"] is True



def test_repeated_pattern_detection():

    result = analyze_password("aaaaaa123!")


    assert result["has_repeated_pattern"] is True



def test_strong_password_analysis():

    result = analyze_password("N7@xLm92#Qp45")


    assert result["is_common_password"] is False

    assert result["has_repeated_pattern"] is False

    assert result["has_sequential_pattern"] is False