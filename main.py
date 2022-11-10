from config import CipherAction
from crypt import encrypt_file, decrypt_file
from services import input_filename, make_data_folder, next_cipher


def main():
    try:
        action_number = int(input(
            "Enter action number\n1 — Encrypt File\n2 — Decrypt File\n>>> "
        ).strip())

    except ValueError:
        print("Action number must have an integer type")
        return main()

    filename = input_filename()
    password = input(f"{'-' * 24}\nNow enter password >>> ")

    if action_number == CipherAction.ENCRYPT:
        encrypt_file(filename, password)

    elif action_number == CipherAction.DECRYPT:
        decrypt_file(filename, password)

    if next_cipher():
        return main()


if __name__ == "__main__":
    try:
        make_data_folder()
        main()
    except KeyboardInterrupt:
        print("Execution stopped")
