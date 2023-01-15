"""
GC26	
35	
DRUNKOMETER	
Write a program that checks somebody is competent to operate machinery in the nuclear factory by insisting that they type the same phrase twice. You can choose the phrase. Make sure it's twisty!	
"""

Phrase = "Mourinho"

Phrase1 = input("Phrase 1: ")
Phrase2 = input("Re-enter Phrase again: ")

x= 0
while (Phrase1 != Phrase or Phrase1 != Phrase2) and x != 5:
  print("\nYou got",5-x,"times left to re-enter the correct word\n")
  x += 1
  Phrase1 = input("Phrase 1: ")
  Phrase2 = input("Re-enter Phrase again: ") 
  

if x== 5:
  print("You're not competent to handle machinery today")
else:
  print("You can handle machinery")
