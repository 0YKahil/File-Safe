"""
file_encrypt.py
author: YKahil
"""

import os
from cryptography.fernet import Fernet



# contains the desired contents to be encrypted (by encrypt function)
contents_toEncrypt = []

# contains the desired contents to be decrypted (by decrypt function)
contents_toDecrypt = []

# **IMPORTANT** key is the key encrypt_files will encrypt using, meaning it is the only
# key to decrypt the files later
key = Fernet.generate_key()

# key_files will contain all the names of the ".key" files in the directory 
# to not encrypt keys and allow safe decryptions if files were encrypted multiple times
key_files = []

def select_contents(path: str) -> list[str]:
    """
    returns a list of the names of the files (not folders) in the desired path,
    appends any .key files found to key_files
    """
    file_list = []
    for file in os.listdir(path):
        # ensuring program does not encrypt itself
        if file == "file_encrypt.py" or file == "file_encryptor.exe":
            continue
        
        # appends any .key file to key_files for track keeping
        if file[len(file)-4:] == ".key":
            key_files.append(file)
        
        else:
            file_list.append(file)
            
    return file_list

def decrypt_files(desired_files: list[str]) -> None:
    """
    Takes a list of string with the names of the files to decrypt and decrypts them
    returns None
    """
    with open("unlock_key1.key", "rb") as key:
        unlock_key = key.read()
        
    for file in desired_files:
        # reading contents of all desired files and decrypting them
        with open(file, "rb") as desired_file:
            file_contents = desired_file.read()
        decrypted_contents = Fernet(unlock_key).decrypt(file_contents)
        
        with open(file, "wb") as desired_file:
            desired_file.write(decrypted_contents)
            
        print("decrypted")
        
        
        
def encrypt_files(desired_files: list[str]) -> None:
    """
    Takes a list of string with the names of the files to encrypt and encrypts them
    returns None
    """
    current_key = str(len(key_files) + 1)
    
    # Writes a .key file containing the unlock key that was genereted to encrypt with
    # using current_key to ensure that the file name will be numbered as the nth time
    # the file was encrypted. 
    # This ensures there will be no key overwrites and keeps track of
    # which encryption required which key.
    with open("unlock_key"+ current_key + ".key", "wb") as unlock_key:
        unlock_key.write(key)
    
    for file in desired_files:
        # reading contents of all desired files and encrypting them
        with open(file, "rb") as desired_file:
            file_contents = desired_file.read()
        encrypted_contents = Fernet(key).encrypt(file_contents)
        
        with open(file, "wb") as desired_file:
            desired_file.write(encrypted_contents)
            
        print("encrypted")



def main() -> None:
    print("\n\t\t\t**File Encryptor**\n\n")
    print("""***Disclaimer: The author and contributors of this file encryption script 
          are not responsible for any misuse, unauthorized access, or 
          illegal activities associated with its usage. Users are encouraged to comply 
          with applicable laws, exercise ethical judgment, and assume full accountability 
          for their actions. 
          This script is provided for educational and legitimate purposes only.***\n\n""")
    
    input("Press Enter to continue...\n")
    
    running = True
    while running:
        action = input("Select an option... \n\n 1) Encrypt Files \n 2) Decrypt Files \n(input number of choice or exit) \n > ")
        if choice.lower() == "exit":
                running = False
                quit()
        if action == "1":
            path = input("please input your desired directory to encrypt (../path/...): \n> ")
            choice = input("Are you sure you want to encrypt ALL files at " + path + "? Type 'AGREE' to continue\n > ")
            if choice.lower() == "exit":
                running = False
                quit()
            if choice != "AGREE":
                print("did not recieve 'AGREE'")
                running = False
                
            else:
                print(select_contents(path))
                encrypt_files(select_contents(path))
                running = False
                break

        if action == "2":
            if choice.lower() == "exit":
                running = False
                quit()
            path = input("please input your desired directory to decrypt (../path/...): \n> ")
            choice = input("Are you sure you want to decrypt ALL files at" + path + "? Type 'AGREE' to continue\n > ")
            if choice != "AGREE":
                print("did not recieve 'AGREE'")
                running = False
            else:
                try:
                    print(select_contents(path))
                    decrypt_files(select_contents(path))
                    running = False
                    break
                except:
                    print("Error (did you type the path correctly?)")
                    break
    
    
main()
