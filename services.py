import os
import sys
from config import DATA_FOLDER


def make_data_folder() -> None:
    if not os.path.exists(DATA_FOLDER):
        os.mkdir(DATA_FOLDER)


def input_filename() -> str:
    filename = input("Load file in «data» folder and enter "
                     "filename with extension\n>>> ")

    if filename not in os.listdir(DATA_FOLDER):
        print(f"File «{filename}» not found in «data» folder. Try again...")
        return input_filename()

    return filename


def next_cipher():
    action_number = input("1 — next\n2 — quit\n>>> ")
    if action_number in {"1", "2"}:
        return True if action_number == "1" else sys.exit(1)

    return next_cipher()
