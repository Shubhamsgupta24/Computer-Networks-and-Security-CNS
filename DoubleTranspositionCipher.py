from itertools import permutations

def create_matrix(text, rows, cols):
    matrix = [['' for _ in range(cols)] for _ in range(rows)]
    idx = 0
    for r in range(rows):
        for c in range(cols):
            if idx < len(text):
                matrix[r][c] = text[idx]
                idx += 1
    return matrix

def pad_plaintext(plaintext, rows, cols):
    padded_length = rows * cols
    if len(plaintext) < padded_length:
        plaintext += 'X' * (padded_length - len(plaintext))
    return plaintext

def encrypt_double_transposition(plaintext, row_perm, col_perm):
    rows = len(row_perm)
    cols = len(col_perm)
    
    plaintext = pad_plaintext(plaintext, rows, cols)
    
    matrix = create_matrix(plaintext, rows, cols)
    
    transposed_matrix = [matrix[row_perm[i]] for i in range(rows)]
    
    encrypted_text = ''
    for r in range(rows):
        for c in range(cols):
            encrypted_text += transposed_matrix[r][col_perm[c]]
    
    return encrypted_text

def decrypt_double_transposition(ciphertext, row_perm, col_perm):
    rows = len(row_perm)
    cols = len(col_perm)
    
    matrix = [['' for _ in range(cols)] for _ in range(rows)]
    
    col_perm_inverse = [0] * cols
    for i, p in enumerate(col_perm):
        col_perm_inverse[p] = i
    
    idx = 0
    for r in range(rows):
        for c in range(cols):
            matrix[r][col_perm_inverse[c]] = ciphertext[idx]
            idx += 1
    
    row_perm_inverse = [0] * rows
    for i, p in enumerate(row_perm):
        row_perm_inverse[p] = i
    
    decrypted_text = ''
    for i in range(rows):
        decrypted_text += ''.join(matrix[row_perm_inverse[i]])
    
    decrypted_text = decrypted_text.rstrip('X')
    
    return decrypted_text


def cryptanalysis_double_transposition(ciphertext, plaintext, possible_perms):
    for row_perm in possible_perms:
        for col_perm in possible_perms:
            decrypted_text = decrypt_double_transposition(ciphertext, row_perm, col_perm)
            if decrypted_text.startswith(plaintext):
                return row_perm, col_perm, decrypted_text
    return None


def generate_permutations(n):
    return list(permutations(range(n)))

plaintext = "Shubham"
row_perm = [2, 0, 1]  
col_perm = [1, 0, 2] 

ciphertext = encrypt_double_transposition(plaintext, row_perm, col_perm)
print("Encrypted text:", ciphertext)

possible_perms = generate_permutations(len(row_perm))

found_row_perm, found_col_perm, decrypted_text = cryptanalysis_double_transposition(ciphertext, plaintext, possible_perms)

print("Found row permutation:", found_row_perm)
print("Found column permutation:", found_col_perm)
print("Decrypted text:", decrypted_text)