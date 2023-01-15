"""
GC41	
25	
DIVIDE BY 3	
Ask for a number and the computer will tell you if you can divide it exactly by 3.
"""

number = int(input("Number: "))
if number % 3 == 0:
  print("Divisible by 3")
else:
  print("Not divisible by 3")
