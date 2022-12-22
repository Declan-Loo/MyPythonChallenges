"""
AS81	50
NUMBER PROCEDURE
Create a procedure that outputs the sum and product of all the numbers in a list
"""
import random

#Procedure to output sum and product of all numbers in a list.
def NumberProcedure(my_list):
    total_sum = 0
    product = 1
    for i in my_list:
        total_sum += i
        product *= i
        
    print("Sum of all numbers in list: %s" % total_sum)
    print("Product of all numbers in list: %s" % product)
    
#Create list using list comprehension
num_list = [random.randint(0,100) for i in range(10)]

#Print the list created before passing list into procedure (function).
print("List given: %s" % num_list)
NumberProcedure(num_list)
