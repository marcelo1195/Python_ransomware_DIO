# File Encryption and Decryption Tool

This project provides a tool for encrypting and decrypting files using Fernet symmetric encryption and RSA asymmetric encryption. The tool generates a Fernet key, encrypts it with an RSA public key, and allows for the encryption and decryption of specified file types.

## Features

- Generate RSA key pairs (public and private).
- Generate a Fernet key for symmetric encryption.
- Encrypt the Fernet key using the RSA public key.
- Encrypt files with specified extensions.
- Decrypt files using the RSA private key and the previously encrypted Fernet key.
- Create an instruction file for users after encryption.

## Directory Structure
project/
│
├── keys/                     # Directory for storing RSA keys and encrypted Fernet key
│   ├── private_key.pem       # RSA private key
│   └── public_key.pem        # RSA public key
│
├── crypt.py                  # Script for generating and saving the encrypted Fernet key
├── decrypt.py                # Script for decrypting files
├── main.py                   # Main script for orchestrating the encryption process
├── RSA_keys.py               # Script for generating RSA keys
└── utils.py                  # Utility functions for directory and file handling



## Usage

1. **Generate RSA Keys:**
   Run the `RSA_keys.py` script to generate the RSA key pair. This will create a `keys` directory containing the public and private keys.

bash
python RSA_keys.py


2. **Encrypt Files:**
   Run the `main.py` script to generate a Fernet key, encrypt it with the RSA public key, and encrypt the specified files in the user's home directory.

bash
python main.py


3. **Decrypt Files:**
   Run the `decrypt.py` script to decrypt the encrypted files using the RSA private key and the previously encrypted Fernet key.

bash
python decrypt.py


## Requirements

- Python 3.x
- `cryptography` library

You can install the required library using pip:

bash
pip install cryptography


## Important Notes

- Ensure that you have the necessary permissions to access and modify the files in the specified directories.
- Use this tool responsibly and only on files you have permission to encrypt or decrypt.
- The instruction file created after encryption contains important information for decrypting the files.

## License

This project is licensed under the MIT License.
