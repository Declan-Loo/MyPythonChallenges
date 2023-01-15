"""
TU06	
12	
IFFY NUMBERS	
Using the If function to sort out numbers
"""

myHeight = 165
PeopleHeight = int(input("What is your height in cm? "))
if myHeight > PeopleHeight:
  print("I'm taller than you :-)")
elif myHeight == PeopleHeight:
  print("We same height")
else:
  print("You're even taller than me :O")
