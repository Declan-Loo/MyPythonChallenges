"""
GC05	
50	
DEMO ALGORITHMS	
Create demo code to demonstrate the ideas of: sequence, selection, repetition & variable.	
"""

def selection(num1,num2):
  if num1 > num2:
    print(num1, "is bigger")
  elif num2 > num1:
    print(num2,"is bigger")
  else:
    print(num1,"and",num2,"are the same")
  print("This is an example of selection as it is an if statement where two variables are compared and given results are outputted if their condition is satisfied")

def repetition(num1,counter):
  for i in range(1,(num1+1),counter):
    print(i)
  print("This shows repetition as it is using a for loop to print a range of numbers with a given interval")

def sequence():
  print("Hi!")
  print("I am Baymax!")
  print("Your personal health companion")
  print("This shows sequence as the statements are printed one at a time")

def variable(x):
  x = 10
  print("x = 10 is an example of initialisation where the variable x is assigned to integer value of 10.")

selection(5,10)

repetition(10,2)

sequence()

variable(10)
