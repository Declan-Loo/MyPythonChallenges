"""
GC48	35	ONLY WHOLE NUMBERS
Validate input using a while loop so that only whole numbers are accepted.	
"""

#Get an input from the user.
number = input("Number?: ")

#While loop to check if the number is an integer. Condition is to see if the number is not an integer.
while number.isdigit() == False:
    #Output error message if the number inputted is not a whole number
    number = input("You have not inputted a whole number. Please try again. Number?: ")
    
#Print the output after validation checks have been satisfied.
print("You have inputted a whole number! Your number is: " +str(number))
    
