from Crypto.PublicKey import RSA

# Generating public and private keys
key = RSA.generate(4096)
private_key = key.export_key()
public_key = key.public_key().export_key()

# Exporting keys
with open("private_key.pem", "wb") as f:
    f.write(private_key)
with open("public_key.pem", "wb") as f:
    f.write(public_key)


