'''
Playfair Cipher Algorithm
'''

def create_cipher_key(shift_value):
    alphabet_chars = 'abcdefghijklmnopqrstuvwxyz'
    shifted_chars = alphabet_chars[shift_value:] + alphabet_chars[:shift_value]
    cipher_key = dict(zip(alphabet_chars, shifted_chars))
    return cipher_key

def perform_encryption(input_message, cipher_key):
    encrypted_result = ''
    for character in input_message:
        if character.isalpha():
            if character.islower():
                encrypted_result += cipher_key[character]
            else:
                encrypted_result += cipher_key[character.lower()].upper()
        else:
            encrypted_result += character
    return encrypted_result

def perform_decryption(ciphertext_input, cipher_key):
    reverse_cipher_key = {v: k for k, v in cipher_key.items()}
    decrypted_result = ''
    for character in ciphertext_input:
        if character.isalpha():
            if character.islower():
                decrypted_result += reverse_cipher_key[character]
            else:
                decrypted_result += reverse_cipher_key[character.lower()].upper()
        else:
            decrypted_result += character
    return decrypted_result

def main():
    shift_value = int(input("Enter the shift value for the cipher: "))
    cipher_key = create_cipher_key(shift_value)
    print(cipher_key)

    user_choice = input("Encrypt or decrypt? (e/d): ").lower()
    if user_choice == 'e':
        input_message = input("Enter the message to encrypt: ")
        encrypted_message = perform_encryption(input_message, cipher_key)
        print("Encrypted message:", encrypted_message)
    elif user_choice == 'd':
        ciphertext_input = input("Enter the message to decrypt: ")
        decrypted_message = perform_decryption(ciphertext_input, cipher_key)
        print("Decrypted message:", decrypted_message)
    else:
        print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")

if __name__ == "__main__":
    main()
