import os
import pyAesCrypt
from config import DATA_FOLDER, DELETE_SOURCE_FILES


def encrypt_file(filename: str, password: str, buffer_size=512 * 1024) -> None:
    filepath = DATA_FOLDER / filename
    pyAesCrypt.encryptFile(infile=filepath,
                           outfile=f"{filepath}.aes",
                           passw=password,
                           bufferSize=buffer_size)
    if DELETE_SOURCE_FILES:
        os.remove(filepath)
    print(f"Data encrypted as {filename}.aes")


def decrypt_file(filename: str, password: str, buffer_size=512 * 1024) -> None:
    from_filepath = DATA_FOLDER / filename
    to_filepath = str(from_filepath)[:-4]
    try:
        pyAesCrypt.decryptFile(infile=from_filepath,
                               outfile=to_filepath,
                               passw=password,
                               bufferSize=buffer_size)
    except ValueError:
        password = input("Wrong password! Try again or type «q»\n>>> ")
        if password in ["q", "exit"]:
            return
        return decrypt_file(filename, password)

    os.remove(from_filepath)
    print(f"Data decrypted in {to_filepath}. Encrypted file was deleted")
