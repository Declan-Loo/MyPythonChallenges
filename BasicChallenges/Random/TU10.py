"""
TU10	25	RANDOM	Learn how to choose random numbers and items
"""

#Exercise 1 
from random import *
mynumber = uniform(0.1, 9.9)
print(mynumber)

import random
Choose_Name = ["James","John","Mark","Rick"]
chosen = random.choice(Choose_Name)
print(chosen)
choice = input("Remove name? ")
if choice in ['yes','Yes','Y','y']:
  Choose_Name.remove(chosen)
print(Choose_Name)
