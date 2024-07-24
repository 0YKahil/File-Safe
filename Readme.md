# File Safe

## File encrypting script

**Description**:
- File Safe is a basic script that encrypts the file (not folder) contents of a given directory
- The script will make use of the cryptography's fernet api to generate a key used to unlock the encrypted files
- The file encryptor will take a passcode before use and this passcode will be used to access the decryption key and decrypt the files using the decryption script


***Disclaimer: The author and contributors of this file encryption script are not responsible for any misuse, unauthorized access, or illegal activities associated with its usage. Users are encouraged to comply with applicable laws, exercise ethical judgment, and assume full accountability for their actions. This script is provided for educational and legitimate purposes only.***

## Usage:

## Windows
### To encrypt
 1. Place file_encrypt.exe (from for_windows) into the folder that holds the files you wish to encrypt
 2. Run file_encrypt.exe
 3. Enter **1** into the console to select **encrypt** as the desired option
 4. Enter the desired path of the file (e.g. C:\Users\USER\Desktop\directory) where directory contains the files to be encrypted
 5. Enter "AGREE" (without " ") in that exact form to confirm the action
 6. Your files in directory will now be inaccessible and encrypted. There will be a keyfile generate that you should keep somewhere safe, you will need this keyfile to unlock the files again (DO NOT LOSE IT).

### To encrypt
 1. If it is not already there, place file_encrypt.exe and **the key file that was previously generated** into the folder that holds the files you wish to decrypt
 2. Run file_encrypt.exe
 3. Enter **2** in the console to select **decrypt** as the desired option
 4. Enter the desired path of the file (e.g. C:\Users\USER\Desktop\directory) where directory contains the files to be decrypted
 5. Enter "AGREE" (without " ") in that exact form to confirm the action
 6. Your files in the directory will now become decrypted and are once again accessible. It is safe to delete the keyfile as the next time the encryption will run it will generate a different one.

## Linux
### To encrypt
 1. Place file_encrypt (from for_linux) into the directory that holds the files you wish to encrypt
 2. Run file_encrypt using the command line in the directory you wish to encrypt (./file_encrypt)
 3. Enter **1** into the console to select **encrypt** as the desired option
 4. Enter the desired path of the file (e.g. /home/user/directory) where directory contains the files to be encrypted
 5. Enter "AGREE" (without " ") in that exact form to confirm the action
 6. Your files in directory will now be inaccessible and encrypted. There will be a keyfile generate that you should keep somewhere safe, you will need this keyfile to unlock the files again (DO NOT LOSE IT).

### To encrypt
 1. If it is not already there, place file_encrypt and **the key file that was previously generated** into the directory that holds the files you wish to decrypt
 2. Run file_encrypt using the command line in the directory you wish to encrypt (./file_encrypt)
 3. Enter **2** in the console to select **decrypt** as the desired option
 4. Enter the desired path of the file (e.g. /home/user/directory) where directory contains the files to be decrypted
 5. Enter "AGREE" (without " ") in that exact form to confirm the action
 6. Your files in the directory will now become decrypted and are once again accessible. It is safe to delete the keyfile as the next time the encryption will run it will generate a different one.



