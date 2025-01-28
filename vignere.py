def vigenere_encrypt(plaintext, key):
    """
    Encrypts the plaintext using the Vigenère cipher.
    """
    encrypted_text = []
    key = key.upper()
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            if char.islower():
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted_text.append(encrypted_char)
            key_index = (key_index + 1) % len(key)
        else:
            encrypted_text.append(char)  # Non-alphabetic characters remain unchanged

    return ''.join(encrypted_text)


def vigenere_decrypt(ciphertext, key):
    """
    Decrypts the ciphertext using the Vigenère cipher.
    """
    decrypted_text = []
    key = key.upper()
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            if char.islower():
                decrypted_char = chr((ord(char) - ord('a') - shift + 26) % 26 + ord('a'))
            else:
                decrypted_char = chr((ord(char) - ord('A') - shift + 26) % 26 + ord('A'))
            decrypted_text.append(decrypted_char)
            key_index = (key_index + 1) % len(key)
        else:
            decrypted_text.append(char)  # Non-alphabetic characters remain unchanged

    return ''.join(decrypted_text)


# Example usage:
plaintext = "HELLO WORLD"
key = "KEY"
ciphertext = vigenere_encrypt(plaintext, key)
print(f"Encrypted: {ciphertext}")

decrypted = vigenere_decrypt(ciphertext, key)
print(f"Decrypted: {decrypted}")
