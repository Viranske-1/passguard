from pathlib import Path


# Project root directory

BASE_DIR = Path(__file__).resolve().parent.parent


# Data directory

DATA_DIR = BASE_DIR / "data"


# Common password database

COMMON_PASSWORD_FILE = DATA_DIR / "common_passwords.txt"