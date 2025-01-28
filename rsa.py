import random
from math import gcd

# Helper function: Generate a random prime number
def generate_prime(start, end):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime = random.randint(start, end)
    while not is_prime(prime):
        prime = random.randint(start, end)
    return prime

# Extended Euclidean Algorithm for modular inverse
def extended_euclidean(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_euclidean(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def mod_inverse(e, phi):
    _, x, _ = extended_euclidean(e, phi)
    return x % phi

# RSA Key Generation
def generate_keys():
    # Step 1: Choose two prime numbers
    p = generate_prime(50, 100)  # You can increase the range for stronger keys
    q = generate_prime(50, 100)
    while p == q:  # Ensure p and q are distinct
        q = generate_prime(50, 100)

    # Step 2: Compute n = p * q and phi = (p-1) * (q-1)
    n = p * q
    phi = (p - 1) * (q - 1)

    # Step 3: Choose e such that 1 < e < phi and gcd(e, phi) = 1
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    # Step 4: Compute d such that (d * e) % phi = 1
    d = mod_inverse(e, phi)

    return (e, n), (d, n)  # Public key (e, n), Private key (d, n)

# RSA Encryption
def encrypt(plaintext, public_key):
    e, n = public_key
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext

# RSA Decryption
def decrypt(ciphertext, private_key):
    d, n = private_key
    plaintext = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return plaintext

# Example Usage
public_key, private_key = generate_keys()
print(f"Public Key: {public_key}")
print(f"Private Key: {private_key}")

# Encrypt and Decrypt a word
message = "PRATIBHA"
print(f"Original Message: {message}")

encrypted = encrypt(message, public_key)
print(f"Encrypted Message: {encrypted}")

decrypted = decrypt(encrypted, private_key)
print(f"Decrypted Message: {decrypted}")
