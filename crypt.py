from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_public_key

def generate_fernet_key():
    return Fernet.generate_key()

def encrypt_fernet_key_with_rsa(fernet_key, public_key_path):
    with open(public_key_path, "rb") as key_file:
        public_key = load_pem_public_key(key_file.read())

    encrypted_key = public_key.encrypt(
        fernet_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted_key

def encrypt_file(file_path, fernet):
    with open(file_path, 'rb') as file:
        file_data = file.read()
    encrypted_data = fernet.encrypt(file_data)
    encrypt_file_path = file_path + '.encrypted'
    with open(encrypt_file_path, 'wb') as file:
        file.write(encrypted_data)
    print(f"Archive encrypted: {encrypt_file_path}")