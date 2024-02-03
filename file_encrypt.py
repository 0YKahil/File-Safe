"""
file_encrypt.py
author: YKahil
"""

import os
from cryptography import fernet

print("\t\t**File Encryptor**")

# contains the desired contents to be encrypted (by encrypt function)
contents_toEncrypt = []

# contains the desired contents to be decrypted (by decrypt function)
contents_toDecrypt = []

def select_contents(path: str) -> list[str]:
    """
    returns a list of the names of the files (not folders) in the desired path
    """
    file_list = []
    file_list = os.listdir(path)
    return file_list


def encrypt_files(desired_files: list[str]) -> None:
    pass


def decrypt_files(desired_files: list[str]) -> None:
    pass


print(select_contents("/home/ykahil/safe/toencrypt"))
