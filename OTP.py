'''
One-Time Pad Algorithm (Vernam Cipher):
This algorithm uses Substitution method wherein the length of key is equal to the legth of the plain text and every alphabet is assigned a number starting from A as 0 uptill Z as 25.
The key is randomnly generated and it is used to encrypt and decrypt a single message.
'''

import random
import string

def generateKey(plain_text):
    key_list = []
    for _ in range(len(plain_text)):
        key_list.append(random.choice(string.ascii_lowercase))
    key = ''.join(key_list)
    return key

def StringEncryption(text,key):
    cipher_list = []
    for i in range(len(key)):
        #Cipher Value is (Key + Text)Mod26 
        cipher_value = ((ord(text[i]) - ord('A')) + (ord(key[i]) - ord('A'))) % 26
        cipher_char = chr(cipher_value + ord('A'))
        cipher_list.append(cipher_char)
    
    cipher_text = ''.join(cipher_list)
    return cipher_text
 
def StringDecryption(cipher_text,key):
    text_list = []
    for i in range(len(key)):
        #Text Value is (CipherText - Key)Mod26
        text_value = ((ord(cipher_text[i]) - ord('A')) - (ord(key[i]) - ord('A'))) % 26
        text_char = chr(text_value + ord('A'))
        text_list.append(text_char)
    text = ''.join(text_list)
    return text

#The plain text has to be encrypted and decrypted
plain_text = "Shubham"

#The key will be generated randomnly for added security
random_key = generateKey(plain_text)

encrypted_text = StringEncryption(plain_text.upper(),random_key.upper())
print(f"Encrypted Text is : {encrypted_text}")

decrypted_text = StringDecryption(encrypted_text,random_key.upper())
print(f"Decrypted Text is : {decrypted_text}")