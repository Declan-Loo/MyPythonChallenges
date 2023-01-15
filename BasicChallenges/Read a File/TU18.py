"""
TU18	
30	
READ A FILE	
Learn how to read a file in Python
"""

import time
choice = input("Which poem do you want to read? ")
print("\n")
if choice in ['Rudyard','rudyard']:
  with open("rudyard.txt","r") as whole_file:
    for line in whole_file:
          print(line,end="")
          time.sleep(2.5)
else:
  with open("mam.txt","r") as whole_file:
    for line in whole_file:
          print(line,end="")
          time.sleep(2)
