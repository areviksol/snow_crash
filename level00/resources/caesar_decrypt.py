"""
This is a Python function to decrypt a message that was encrypted 
using the Caesar cipher, a type of substitution cipher. The Caesar 
cipher works by shifting each letter of the plaintext by a certain 
number of positions down or up the alphabet. The provided code 
attempts to decrypt a ciphertext by trying all possible shifts 
(from 0 to 25), which effectively brute forces the decryption.
"""

def caesar_cipher_decrypt(ciphertext, shift):
    """Decrypts a given ciphertext using a Caesar cipher with the specified shift."""
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            shift_amount = shift
            if char.islower():
                start = ord('a')
            elif char.isupper():
                start = ord('A')
            decrypted_text += chr((ord(char) - start - shift_amount) % 26 + start)
        else:
            decrypted_text += char
    return decrypted_text

ciphertext = "cdiiddwpgswtgt"

for shift in range(26):
    decrypted_text = caesar_cipher_decrypt(ciphertext, shift)
    print(f'Shift {shift}: {decrypted_text}')