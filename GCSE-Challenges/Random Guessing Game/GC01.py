"""
GC01	
50	
RANDOM GUESSING GAME	
Create a game where you guess a number from 1 to 100. The program should tell you if the number is higher or lower and check for non-valid input.	
"""

from random import randint
x =randint(1,100)

while True:
  answer = int(input("Guess: "))
  if answer > x:
    print("Lower\n")
  elif answer < x:
    print("Higher\n")
  else:
    print("Answer is",x)
    break
