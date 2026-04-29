
import hashlib


message= "Hi this is sid"
msg_byte=message.encode()


sha_256_hash=hashlib.sha256(msg_byte)


digest=sha_256_hash.hexdigest()


print("Message",message)
print("SH-256 digest",digest)



# Message Hi this is sid
# SH-256 digest 7618be00b2e24f10e9ddcf7dbd7a50de15f3fe98a864b8114dd356ad363b3883

