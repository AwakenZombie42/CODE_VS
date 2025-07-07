# Ciphertext to decrypt
ciphertext = input("Enter the ciphertext: ")

# Caesar cipher decryption function
def caesar_decrypt(text, shift):
    decrypted = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decrypted += chr((ord(char) - base - shift) % 26 + base)
        else:
            decrypted += char
    return decrypted

# Try all 26 shifts and print results
for shift in range(26):
    decrypted_text = caesar_decrypt(ciphertext, shift)
    print(f"Shift {shift}: {decrypted_text}")