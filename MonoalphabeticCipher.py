'''
Monoalphabetic Algorithm
'''

def convert_to_lowercase(text):
    return text.lower()

def remove_spaces(text):
    cleaned_text = ""
    for char in text:
        if char != " ":
            cleaned_text += char
    return cleaned_text

def create_digraphs(text):
    digraphs = []
    index = 0
    for i in range(2, len(text), 2):
        digraphs.append(text[index:i])
        index = i
    digraphs.append(text[index:])
    return digraphs

def insert_filler_letters(text):
    length = len(text)
    if length % 2 == 0:
        for i in range(0, length, 2):
            if text[i] == text[i+1]:
                text = text[:i+1] + 'x' + text[i+1:]
                return insert_filler_letters(text)
    else:
        for i in range(0, length-1, 2):
            if text[i] == text[i+1]:
                text = text[:i+1] + 'x' + text[i+1:]
                return insert_filler_letters(text)
    return text

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def generate_key_matrix(keyword, alphabet):
    key_chars = []
    for char in keyword:
        if char not in key_chars:
            key_chars.append(char)

    combined_elements = key_chars[:]
    for char in alphabet:
        if char not in combined_elements:
            combined_elements.append(char)

    key_matrix = []
    while combined_elements:
        key_matrix.append(combined_elements[:5])
        combined_elements = combined_elements[5:]

    return key_matrix

def find_position(matrix, element):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == element:
                return row, col

def encrypt_row(matrix, row1, col1, row2, col2):
    char1 = matrix[row1][(col1 + 1) % 5]
    char2 = matrix[row2][(col2 + 1) % 5]
    return char1, char2

def encrypt_column(matrix, row1, col1, row2, col2):
    char1 = matrix[(row1 + 1) % 5][col1]
    char2 = matrix[(row2 + 1) % 5][col2]
    return char1, char2

def encrypt_rectangle(matrix, row1, col1, row2, col2):
    char1 = matrix[row1][col2]
    char2 = matrix[row2][col1]
    return char1, char2

def encrypt_using_playfair(matrix, digraph_list):
    ciphertext_list = []
    for digraph in digraph_list:
        row1, col1 = find_position(matrix, digraph[0])
        row2, col2 = find_position(matrix, digraph[1])

        if row1 == row2:
            char1, char2 = encrypt_row(matrix, row1, col1, row2, col2)
        elif col1 == col2:
            char1, char2 = encrypt_column(matrix, row1, col1, row2, col2)
        else:
            char1, char2 = encrypt_rectangle(matrix, row1, col1, row2, col2)

        ciphertext_list.append(char1 + char2)
    return ciphertext_list

plaintext = 'shubham'
plaintext = remove_spaces(convert_to_lowercase(plaintext))
plaintext_digraphs = create_digraphs(insert_filler_letters(plaintext))

if len(plaintext_digraphs[-1]) != 2:
    plaintext_digraphs[-1] += 'z'

key = "hello"
print("Key:", key)
key = convert_to_lowercase(key)
key_matrix = generate_key_matrix(key, alphabet)

print("Plaintext:", plaintext)
ciphertext_list = encrypt_using_playfair(key_matrix, plaintext_digraphs)

ciphertext = "".join(ciphertext_list)
print("Ciphertext:", ciphertext)