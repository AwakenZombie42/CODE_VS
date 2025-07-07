# Caesar cipher encryption function
def caesar_encrypt(text, shift):
    encrypted = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char
    return encrypted

# Get user input
sentence = input("Enter a sentence to encrypt: ")
shift = int(input("Enter the shift value (0-25): "))

# Encrypt the sentence
encrypted_sentence = caesar_encrypt(sentence, shift)
print("Encrypted sentence:", encrypted_sentence)