# Educational Cryptography Project

## Important Notice

This project is strictly for educational and research purposes only. It demonstrates concepts of cryptography and data security. Using this software for malicious or illegal activities is strictly prohibited and may result in severe legal consequences.

## Overview

This project implements a simple encryption system that demonstrates the basic functioning of ransomware. It uses hybrid cryptography, combining symmetric encryption (Fernet/AES) for files and asymmetric encryption (RSA) to protect the symmetric key.

## Components

1. `crypt.py`: Main script for encrypting files.
2. `decrypt.py`: Script for decrypting files (to be implemented).
3. `utils.py`: Utility functions, including operating system detection.
4. `RSA_keys.py`: Script to generate RSA keys (not included in this repository).
5. `requirements.txt`: List of Python dependencies.

## Requirements

- Python 3.7+
- Required libraries are listed in `requirements.txt`

To install the dependencies, run:
pip install -r requirements.txt


## How to Use

### Preparation

1. Generate an RSA key pair using `RSA_keys.py` (not provided).
2. Save the public key as `public_key.pem` in the project directory.

### Encryption

Run the encryption script:

python crypt.py


This script will:
- Generate a Fernet key.
- Encrypt files in the home directory (Windows) or /home (Linux/macOS).
- Encrypt the Fernet key with the RSA public key.
- Create an instruction file.

### Decryption (Not Implemented)

Decryption requires the corresponding RSA private key. A decryption script would need to:
1. Decrypt the Fernet key using the RSA private key.
2. Use the Fernet key to decrypt the files.

## Packaged Executable

For easier distribution, this project can be packaged into a single executable file using PyInstaller. To create the executable:

1. Install PyInstaller:
pip install pyinstaller


2. Create the executable:
pyinstaller --onefile --windowed --clean --noupx crypt.py


3. The executable will be created in the `dist` directory.

Note: The executable is platform-specific. You'll need to create separate executables for different operating systems.

## Security and Ethics

- This software is a demonstration and should not be used on real systems.
- Encrypting system files can cause irreparable damage.
- Always obtain explicit permission before testing on any system.

## Contributions

Contributions to improve security, efficiency, or educational purposes are welcome. Please open an issue to discuss major changes before submitting a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Disclaimer

The authors are not responsible for any misuse or damage caused by this software. This project is purely for educational and information security research purposes.