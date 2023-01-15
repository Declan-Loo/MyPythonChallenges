"""
TU08	
12	
WHILE TRUE	
Learn how to make loops based on conditionals with this love exercise....
"""

#Exercise 1
while True:
  subject_choice = input("Which subject do you love most? ")
  if subject_choice in ["CS","Computer Science","cs","computer science"]:
    break

number = float(0) #You have to declare this first
while number < 15.0 or number > 20.0 :
    print("Please enter a number between 15 and 20")
    number = float(input("enter a number:"))
