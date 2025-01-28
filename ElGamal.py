import random
from sympy import isprime

def mod_exp(base, exp, mod):
    """Perform modular exponentiation."""
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def generate_prime(bits=10):
    """Generate a random prime number of the specified bit length."""
    while True:
        num = random.randint(2**(bits-1), 2**bits - 1)
        if isprime(num):
            return num

def elgamal_encrypt(plain_text, e1, e2, p, r):
    """Encrypt the plaintext string using ElGamal encryption."""
    c1 = mod_exp(e1, r, p)
    c2 = [(ord(char) * mod_exp(e2, r, p)) % p for char in plain_text]
    return c1, c2

def elgamal_decrypt(c1, c2, p, d):
    """Decrypt the ciphertext back to the plaintext string."""
    s = mod_exp(c1, d, p)
    s_inv = pow(s, -1, p)  # Modular multiplicative inverse of s mod p
    plain_text = ''.join([chr((char * s_inv) % p) for char in c2])
    return plain_text

def main():
    # Input plaintext
    plain_text = input("Enter the plaintext: ")

    # Generate large prime number p
    p = generate_prime(bits=16)
    
    # Choose e1 (primitive root) and private key d
    e1 = random.randint(2, p - 2)
    d = random.randint(2, p - 2)
    
    # Compute e2 = (e1^d) mod p
    e2 = mod_exp(e1, d, p)

    # Choose random r
    r = random.randint(2, p - 2)

    # Encrypt the plaintext
    c1, c2 = elgamal_encrypt(plain_text, e1, e2, p, r)
    
    # Decrypt the ciphertext
    decrypted_text = elgamal_decrypt(c1, c2, p, d)

    # Display results
    print("\nElGamal Encryption")
    print(f"Prime number (p): {p}")
    print(f"Primitive root (e1): {e1}")
    print(f"Private key (d): {d}")
    print(f"Public key (e2): {e2}")
    print(f"Random number (r): {r}")
    print(f"Ciphertext (c1, c2): ({c1}, {c2})")
    print(f"Decrypted text: {decrypted_text}")

if __name__ == "__main__":
    main()
