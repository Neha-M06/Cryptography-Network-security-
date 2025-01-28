def vigenere_encrypt(plaintext, key):
    ciphertext = ""
    key_index = 0
    key = key.upper()

    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            if char.isupper():
                ciphertext += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                ciphertext += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            key_index = (key_index + 1) % len(key)
        else:
            ciphertext += char
    return ciphertext


def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    key_index = 0
    key = key.upper()

    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            if char.isupper():
                plaintext += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                plaintext += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            key_index = (key_index + 1) % len(key)
        else:
            plaintext += char
    return plaintext


if __name__ == "__main__":
    print("Vigenère Cipher")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()

    if choice in ['E', 'D']:
        text = input("Enter the text: ").strip()
        key = input("Enter the key: ").strip()
        
        if choice == 'E':
            result = vigenere_encrypt(text, key)
            print("Encrypted Text:", result)
        else:
            result = vigenere_decrypt(text, key)
            print("Decrypted Text:", result)
    else:
        print("Invalid choice. Please select either 'E' or 'D'.")
