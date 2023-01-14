"""
GC13	50	ISBN CALCULATOR	
A good example of a check digit is the ISBN 13 found on books. Can you make an ISBN calculator?
"""

#Get user input for Barcode.
ISBNBarcode = input("Barcode?: ")

#Validate the length of the input.
while len(ISBNBarcode) != 13:
    ISBNBarcode = input("Invalid barcode. Please enter appropriate barcode correctly. Barcode?: ")

#Initialise total variable.
total = 0

#Iterate over length of barcode (divided by 2).
for digits in range(len(ISBNBarcode)//2):
    #Do calculations (add to total)
    total += int(ISBNBarcode[digits]) * 1
    total += int(ISBNBarcode[digits*2]) * 3

#Find remainder by doing modulo-10 operation on total.
remainder = total % 10

#Check if remainder is 0.
if remainder == 0:
    #If 0, check if the last digit of Barcode is 0.
    if remainder == int(ISBNBarcode[-1]):
        print("Valid ISBN barcode")
    else:
        print("Invalid ISBN barcode")
else:
    #Calculate check digit and check if check digit matches last number of ISBN barcode.
    check_digit =  10-remainder
    if check_digit == int(ISBNBarcode[-1]):
        print("Valid ISBN barcode")
    else:
        print("Invalid ISBN barcode")
