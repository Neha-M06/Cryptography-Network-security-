
# affine_cipher.py
from math import gcd

def modular_inverse(a, m):
    """
    Finds the modular inverse of a under modulo m using the extended Euclidean algorithm.
    Returns None if the modular inverse does not exist.
    """
    if gcd(a, m) != 1:
        return None  # Inverse doesn't exist if a and m are not coprime
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def affine_encrypt(plaintext, a, b):
    """
    Encrypts the given plaintext using the Affine Cipher.
    """
    m = 26  # Size of the alphabet
    if gcd(a, m) != 1:
        raise ValueError("'a' must be coprime with 26.")

    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            x = ord(char) - offset
            encrypted_char = (a * x + b) % m + offset
            ciphertext += chr(encrypted_char)
        else:
            ciphertext += char
    return ciphertext

def affine_decrypt(ciphertext, a, b):
    """
    Decrypts the given ciphertext using the Affine Cipher.
    """
    m = 26  # Size of the alphabet
    a_inv = modular_inverse(a, m)
    if a_inv is None:
        raise ValueError("'a' has no modular inverse under modulo 26.")

    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            y = ord(char) - offset
            decrypted_char = (a_inv * (y - b)) % m + offset
            plaintext += chr(decrypted_char)
        else:
            plaintext += char
    return plaintext

# Example usage
def main():
    plaintext = "AffineCipherExample"
    a, b = 5, 8

    print("Plaintext:", plaintext)

    encrypted = affine_encrypt(plaintext, a, b)
    print("Encrypted:", encrypted)

    decrypted = affine_decrypt(encrypted, a, b)
    print("Decrypted:", decrypted)

if __name__ == "__main__":
    main()
