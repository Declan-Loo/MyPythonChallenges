"""
GC24	50	
ARE YOU SURE THAT'S A NUMBER?	
Write a small program to check that input is a float and generate an error if it is not.
"""

#Get input from user.
x = input("Input: ")

#Check if input can be converted to a float.
if x.isfloat() == True:
    print("Input is a float")
#Output for error message.
else:
    print("Input is not a float")
    
