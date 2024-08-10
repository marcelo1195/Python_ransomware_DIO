from Crypto.PublicKey import RSA
import os
def generate_and_save_keys():
    keys_dir = 'keys'
    if not  os.path.exists(keys_dir):
        os.makedirs(keys_dir)

    # Generating public and private keys
    key = RSA.generate(4096)

    # Save private key
    private_key = key.export_key()
    with open(os.path.join(keys_dir, 'private_key.pem'), 'wb') as f:
        f.write(private_key)

    # Save public key
    public_key = key.public_key().export_key()
    with open(os.path.join(keys_dir, 'publick_key.pem'), 'wb') as f:
        f.write(public_key)

if __name__ == "__main__":
    generate_and_save_keys()


