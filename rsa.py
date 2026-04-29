
p=17
q=11
e=9
M=10


#calculating n
n=p *q
#calculating phi
phi=(p-1) *(q-1)



# this is the private key d
def mod(e,phi):
    for d in range(1,phi):
        if(e*d) % phi==1:
            return d
d=mod(e,phi)


C=pow(M,e,n) # for encryption
decrypt_m=pow(C,d,n) # for decryption


print("p =", p, ", q =", q)
print("n =", n)
print("phi(n) =", phi)
print("Public key (e) =", e)
print("Private key (d) =", d)

print("\nOriginal Message =", M)
print("Encrypted Message =", C)
print("Decrypted Message =", decrypt_m)

# p = 17 , q = 11
# n = 187
# phi(n) = 160
# Public key (e) = 9
# Private key (d) = 89

# Original Message = 10
# Encrypted Message = 109
# Decrypted Message = 10





