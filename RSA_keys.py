import os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def generate_and_save_keys():
    #Create directory "keys" if not exists
    keys_dir = 'keys'
    if not os.path.exists(keys_dir):
        os.makedirs(keys_dir)

    #Generate keys
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()

    # Saving private key
    with open(os.path.join(keys_dir, 'private_key.pem'), 'wb') as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ))

    # Saving public key
    with open(os.path.join(keys_dir, 'public_key.pem'), 'wb') as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))

if __name__ == "__main__":
    generate_and_save_keys()


