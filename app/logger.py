import logging
from pathlib import Path



LOG_DIR = Path(__file__).resolve().parent.parent / "logs"

LOG_FILE = LOG_DIR / "passguard.log"



LOG_DIR.mkdir(exist_ok=True)



logging.basicConfig(

    filename=LOG_FILE,

    level=logging.INFO,

    format="%(asctime)s - %(levelname)s - %(message)s",

    force=True

)



logger = logging.getLogger("PassGuard")
