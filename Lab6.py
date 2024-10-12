import string

def vigenere_sq():
    alphabet = string.ascii_uppercase
    print("   " + " ".join(alphabet))
    print("  +" + "-" * 51)
    for i, letter in enumerate(alphabet):
        row = [alphabet[(i + j) % 26] for j in range(26)]
        print(f"{letter} | {' '.join(row)}")

def letter_to_index(letter, alphabet):
    return alphabet.index(letter.upper())

def index_to_letter(index, alphabet):
    return alphabet[index % 26]

def vigenere_index(key_letter, plaintext_letter, alphabet):
    key_index = letter_to_index(key_letter, alphabet)
    plaintext_index = letter_to_index(plaintext_letter, alphabet)
    cipher_index = (key_index + plaintext_index) % 26
    return index_to_letter(cipher_index, alphabet)

def encrypt_vigenere(key, plaintext, alphabet):
    key = key.upper()
    plaintext = plaintext.upper()
    ciphertext = ""
    for i, letter in enumerate(plaintext):
        if letter in alphabet:
            key_letter = key[i % len(key)]
            ciphertext += vigenere_index(key_letter, letter, alphabet)
        else:
            ciphertext += letter
    return ciphertext

def undo_vigenere_index(key_letter, cipher_letter, alphabet):
    key_index = letter_to_index(key_letter, alphabet)
    cipher_index = letter_to_index(cipher_letter, alphabet)
    plaintext_index = (cipher_index - key_index) % 26
    return index_to_letter(plaintext_index, alphabet)

def decrypt_vigenere(key, ciphertext, alphabet):
    key = key.upper()
    ciphertext = ciphertext.upper()
    plaintext = ""
    for i, letter in enumerate(ciphertext):
        if letter in alphabet:
            key_letter = key[i % len(key)]
            plaintext += undo_vigenere_index(key_letter, letter, alphabet)
        else:
            plaintext += letter
    return plaintext

def main():
    alphabet = string.ascii_uppercase
    while True:
        print("\nVigenère Cipher")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Print Vigenère Square")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            plaintext = input("Enter the plaintext: ")
            key = input("Enter the key: ")
            ciphertext = encrypt_vigenere(key, plaintext, alphabet)
            print(f"Encrypted text: {ciphertext}")
        elif choice == '2':
            ciphertext = input("Enter the ciphertext: ")
            key = input("Enter the key: ")
            plaintext = decrypt_vigenere(key, ciphertext, alphabet)
            print(f"Decrypted text: {plaintext}")
        elif choice == '3':
            vigenere_sq()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()