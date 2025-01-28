import random

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_keys():
    while True:
        p = int(input("Enter a prime number (p): "))
        if is_prime(p):
            break
        print("The number is not prime. Please try again.")
    
    while True:
        q = int(input("Enter another prime number (q): "))
        if is_prime(q) and q != p:
            break
        print("The number is either not prime or equal to p. Please try again.")
    
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)
    
    d = pow(e, -1, phi)
    return (e, n), (d, n)

def encrypt(plaintext, public_key):
    e, n = public_key
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext

def decrypt(ciphertext, private_key):
    d, n = private_key
    plaintext = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return plaintext

if __name__ == "__main__":
    print("RSA Encryption/Decryption")
    public_key, private_key = generate_keys()
    
    print(f"Public Key: {public_key}")
    print(f"Private Key: {private_key}")
    
    plaintext = input("Enter the plaintext to encrypt: ")
    ciphertext = encrypt(plaintext, public_key)
    print(f"Encrypted message: {ciphertext}")
    
    decrypted_text = decrypt(ciphertext, private_key)
    print(f"Decrypted message: {decrypted_text}")
