"""
GC42	
50	
RANDOM NUMBER LIST	
Use the random function to create a LIST (array) of 50 random numbers that you can use to calculate the Minimum, Maximum and mean average.	
"""

from random import randint
number_list = []
sum_number = 0
for i in range(51):
  number = randint(1,1000)
  sum_number += number
  number_list.append(number)
  
print("Minimum:",min(number_list))
print("Maximum:",max(number_list))
print("Mean average:",(sum_number / 50))
