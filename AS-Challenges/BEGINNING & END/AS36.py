"""
AS36	50	
BEGINNING & END	
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list.	
"""

my_list = [int(number) for number in input("Please insert numbers separated by spaces: ").split()]

print(my_list)

new_list = []
first = my_list[0]
second = my_list[-1]

new_list.append(first)
new_list.append(second)
print("First and last numbers in list:",new_list)
