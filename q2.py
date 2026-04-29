
import hashlib


message="HELLO WORLD"
msg_byte=message.encode()


sha_256_hash=hashlib.sha256(message.encode()).hexdigest()

print("Original Message is :", message)
print("SHA-256 Hash (Encrypted):", sha_256_hash)

check_message="HELLO WORLD"
check_hash=hashlib.sha256(check_message.encode()).hexdigest()

if check_hash == sha_256_hash:
    print("Decryption Successful Message is Verified)")
else:
    print("Decryption Failed (msg is tampered)")


# Original Message is : HELLO WORLD
# SHA-256 Hash (Encrypted): 787ec76dcafd20c1908eb0936a12f91edd105ab5cd7ecc2b1ae2032648345dff
# Decryption Successful Message is Verified)