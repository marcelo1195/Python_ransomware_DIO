from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_private_key

def decrypt_fernet_key_with_rsa(encrypted_fernet_key, private_key_path):
    with open(private_key_path, "rb") as key_file:
        private_key = load_pem_private_key(key_file.read(), password=None)

    fernet_key = private_key.decrypt(
        encrypted_fernet_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return fernet_key

def decrypt_file(file_path, fernet):
    if not file_path.endswith('encrypted'):
        print(f"Pulando arquivo não criptografado: {file_path}")
        return

    with open(file_path, 'rb') as file:
        encrypted_data = file.read()
    try:
        decrypted_data = fernet.decrypt(encrypted_data)
        decrypted_file_path = file_path[:-10]  # Remove '.encrypted'
        with open(decrypted_file_path, 'wb') as file:
            file.write(decrypted_data)
        print(f"Arquivo descriptografado: {decrypted_file_path}")
    except Exception as e:
        print(f"Erro ao descriptografar {file_path}: {e}")