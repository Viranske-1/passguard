import sys
from pathlib import Path


sys.path.append(
    str(Path(__file__).resolve().parent.parent / "app")
)


from logger import logger, LOG_FILE



def test_log_file_creation():

    logger.info("Test log message")


    assert LOG_FILE.exists()



def test_logger_writes_message():

    logger.info("Testing PassGuard logger")


    with open(LOG_FILE, "r") as file:

        content = file.read()


    assert "Testing PassGuard logger" in content