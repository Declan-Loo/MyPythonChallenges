"""
AS57	
50	
VALIDATE A BYTE	
Create a Parity Byte entry system generator that uses even parity.
"""

def parity_checker(byte):
    even_bits = 0
    if len(str(byte)) != 8:
        return "Please retry again with a proper byte input."
    for bit in str(byte):
        if bit == '1':
            even_bits += 1
            
    return even_bits

user_byte = int(input("Please enter byte (NOTE this checker uses Even Parity): "))

if parity_checker(user_byte):
    print("Accepted. Parity check passed.")
else:
    print("Denied. Parity check has failed.")
            
