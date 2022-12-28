"""
AS07	100	
CAESAR CIPHER	
Create a Caesar Cipher encoder and decoder.	
"""

def encode(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        #Check if character is alphabetic or not
        if char.isalpha():
            # Encrypt upper case characters in plaintext
            if char.islower():
                ciphertext += chr((ord(char) + shift - 97) % 26 + 97)
            # Encrypt lower case characters in plaintext
            elif char.isupper():
                ciphertext += chr((ord(char) + shift-65) % 26 + 65)
        else:
            # Do not shift non-alphabetic characters
            ciphertext += char
    return ciphertext

def decode(ciphertext, shift):
    # Use the same shift value to decode the ciphertext as was used to encode it
    return encode(ciphertext, -shift)

# Test the encode and decode functions
plaintext = "Hello there!"
shift = 5
ciphertext = encode(plaintext, shift)
print(ciphertext)  # prints "Mjqqt ymjwj!"
decoded = decode(ciphertext, shift)
print(decoded)  # prints "Hello there!"
