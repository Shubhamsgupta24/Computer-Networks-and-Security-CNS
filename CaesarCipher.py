'''
Caesar Cipher Algorithm:

'''

def caesar_encrypt(plain_text, shift):
    encrypted_list = []
    for char in plain_text:
        if char.isupper():
            encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        encrypted_list.append(encrypted_char)

    encrypted_text = ''.join(encrypted_list)
    return encrypted_text

def caesar_decrypt(encrypted_text, shift):
    decrypted_list = []
    for char in encrypted_text:
        if char.isupper():
            decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        decrypted_list.append(decrypted_char)

    decrypted_text = ''.join(decrypted_list)
    return decrypted_text

# The plain text to be encrypted and decrypted
plain_text = "Shubham"

# Shift value for Caesar Cipher
shift_value = 3

# Encrypting the text
encrypted_text = caesar_encrypt(plain_text, shift_value)
print(f"Encrypted Text: {encrypted_text}")

# Decrypting the text
decrypted_text = caesar_decrypt(encrypted_text, shift_value)
print(f"Decrypted Text: {decrypted_text}")
