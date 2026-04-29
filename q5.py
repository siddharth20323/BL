# %%
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa,padding

# %%
private_key=rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key=private_key.public_key()

# %%
message = b"Hello, this is sid and this is a signed document"

# %%
signature=private_key.sign( #here msg is hashed using sha256, hash is encrypted using private key and signature is created
    message, 
    padding.PSS(
    mgf=padding.MGF1(hashes.SHA256()),
    salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)
print("document :", message.decode())
print("signature created\n")

# %%
try:
    public_key.verify( #here reciever hashes the msg again and verifies it with public key if both match then it is valid
        signature,
        message,
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
    )
    print("Signature valid")
except:
    print("Signature invalid")

# %%


# document : Hello, this is sid and this is a signed document
# signature created

# # %%
# Signature valid