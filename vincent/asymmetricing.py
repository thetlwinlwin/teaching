from cryptography.hazmat.primitives import asymmetric, hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

# Load the public key
with open("public_key.pem", "rb") as f:
    public_key = serialization.load_pem_public_key(f.read())

    message = b"You fucking stupid"

    # Encrypt the message
    ciphertext = public_key.encrypt(  # type: ignore
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    print(ciphertext)
