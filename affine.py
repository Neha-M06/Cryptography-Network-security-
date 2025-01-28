# Function to find modular inverse
def modular_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Function to encrypt text using the Affine Cipher
def affine_encrypt(text, a, b):
    result = ""
    for char in text:
        if char.isalpha():  # Encrypt only alphabetic characters
            if char.isupper():
                result += chr(((a * (ord(char) - 65) + b) % 26) + 65)
            else:
                result += chr(((a * (ord(char) - 97) + b) % 26) + 97)
        else:
            result += char  # Non-alphabetic characters are not encrypted
    return result

# Function to decrypt text using the Affine Cipher
def affine_decrypt(text, a, b):
    a_inverse = modular_inverse(a, 26)
    if a_inverse is None:
        raise ValueError("Multiplicative inverse for 'a' does not exist. Choose a different value of 'a'.")
    result = ""
    for char in text:
        if char.isalpha():  # Decrypt only alphabetic characters
            if char.isupper():
                result += chr(((a_inverse * ((ord(char) - 65) - b)) % 26) + 65)
            else:
                result += chr(((a_inverse * ((ord(char) - 97) - b)) % 26) + 97)
        else:
            result += char  # Non-alphabetic characters are not decrypted
    return result

# Main function to get input from the user
def main():
    print("Affine Cipher")
    print("1: Encrypt")
    print("2: Decrypt")
    choice = input("Choose an option (1 or 2): ")

    if choice not in ["1", "2"]:
        print("Invalid choice.")
        return

    text = input("Enter the text: ")
    a = int(input("Enter the value of 'a' (must be coprime with 26): "))
    b = int(input("Enter the value of 'b': "))

    # Ensure 'a' is coprime with 26
    if modular_inverse(a, 26) is None:
        print("'a' must be coprime with 26. Try again.")
        return

    if choice == "1":
        encrypted_text = affine_encrypt(text, a, b)
        print("Encrypted Text:", encrypted_text)
    elif choice == "2":

        decrypted_text = affine_decrypt(text, a, b)
        print("Decrypted Text:", decrypted_text)

if __name__ == "__main__":
    main()
