import random

# Helper: Modular exponentiation
def modular_exponentiation(base, exp, mod):
    return pow(base, exp, mod)

# Helper: Generate a random prime number
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

# ElGamal Key Generation
def generate_keys():
    # Step 1: Choose a large prime p
    p = generate_prime(100, 200)  # For simplicity; use larger primes in practice

    # Step 2: Choose a generator e1 (primitive root modulo p)
    e1 = random.randint(2, p - 2)

    # Step 3: Choose a private key d (1 <= d <= p-2)
    d = random.randint(1, p - 2)

    # Step 4: Compute e2 = (e1^d) mod p
    e2 = modular_exponentiation(e1, d, p)

    return p, e1, e2, d  # Public key: (p, e1, e2); Private key: d

# ElGamal Encryption
def encrypt(message, public_key):
    p, e1, e2 = public_key
    r = random.randint(1, p - 2)  # Random integer 1 <= r <= p-2

    # Step 1: Compute c1 = (e1^r) mod p
    c1 = modular_exponentiation(e1, r, p)

    # Step 2: Compute c2 = (m * (e2^r)) mod p for each character in the message
    c2 = [(ord(char) * modular_exponentiation(e2, r, p)) % p for char in message]

    return c1, c2, r

# ElGamal Decryption
def decrypt(c1, c2, private_key, p):
    d = private_key

    # Step 1: Compute (c1^d) mod p
    c1_d = modular_exponentiation(c1, d, p)

    # Step 2: Compute the modular inverse of (c1^d) mod p
    c1_d_inverse = pow(c1_d, -1, p)

    # Step 3: Recover the original message
    message = ''.join([chr((char * c1_d_inverse) % p) for char in c2])

    return message

# Example Usage
p, e1, e2, d = generate_keys()
print(f"Public Key: (p={p}, e1={e1}, e2={e2})")
print(f"Private Key: d={d}")

# Encrypt a message
message = "WONDERFUL"
print(f"Original Message: {message}")

c1, c2, r = encrypt(message, (p, e1, e2))
print(f"Ciphertext: c1={c1}, c2={c2}, r={r}")

# Decrypt the message
decrypted_message = decrypt(c1, c2, d, p)
print(f"Decrypted Message: {decrypted_message}")
