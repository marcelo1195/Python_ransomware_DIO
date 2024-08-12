# Conceptual Ransomware Project

## IMPORTANT DISCLAIMER

This project is a CONCEPTUAL IMPLEMENTATION of ransomware for EDUCATIONAL PURPOSES ONLY. It is designed to demonstrate the principles of encryption and file system manipulation in a controlled environment. 

**WARNING:** 
- This software is potentially harmful if misused.
- The author(s) are NOT responsible for any damage caused by this software.
- Using this software for malicious purposes is illegal and unethical.
- DO NOT use this on any system or files without explicit permission.

## Overview

This project implements a basic ransomware-like system using Python. It uses hybrid cryptography, combining Fernet (symmetric) encryption for files and RSA (asymmetric) encryption for key protection.

## Components

1. **RSA_keys.py**
   - Generates RSA key pairs (public and private).
   - Creates a 'keys' directory to store the generated keys.

2. **crypt.py**
   - Generates a Fernet key for symmetric encryption.
   - Encrypts the Fernet key using the RSA public key.
   - Provides functionality to encrypt individual files.

3. **decrypt.py**
   - Decrypts the Fernet key using the RSA private key.
   - Provides functionality to decrypt files encrypted by the system.

4. **main.py**
   - Main orchestrator of the encryption process.
   - Implements the `SimpleCrypter` class which:
     - Generates and manages encryption keys.
     - Encrypts files in specified directories.
     - Creates an instruction file for the "victim".

5. **utils.py**
   - Contains utility functions for:
     - Determining the operating system.
     - Getting the home directory.
     - Iterating through files and directories.

## Usage (For Educational Purposes Only)

1. Generate RSA keys:
python RSA_keys.py


2. Run the encryption process:
python main.py


3. To decrypt (after encryption):
python decrypt.py


## Technical Details

- Uses Fernet for symmetric file encryption.
- Employs RSA for asymmetric encryption of the Fernet key.
- Targets files in the user's home directory.
- Can be configured to target specific file extensions or all files.

## Requirements

- Python 3.x
- cryptography library

## Ethical Considerations

This project is meant to educate about cybersecurity concepts. It should only be used in controlled, authorized environments. Unauthorized use of ransomware or any malicious software is a serious crime.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Disclaimer

The authors of this project are not responsible for any misuse or damage caused by this software. It is provided as-is for educational purposes only.
