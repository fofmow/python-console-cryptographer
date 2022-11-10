from pathlib import Path
from typing import NamedTuple

DATA_FOLDER = Path(__file__).resolve().parent / "data"


class CipherAction(NamedTuple):
    ENCRYPT = 1
    DECRYPT = 2


DELETE_SOURCE_FILES = False
