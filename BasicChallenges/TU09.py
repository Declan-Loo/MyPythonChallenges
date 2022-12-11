"""
ESCAPE CODES
CODE: TU09 POINTS: 12
"""

#Exercise 1: Use the code above, but count the number of times that somebody enters an error! Don't let them get away with it.
count = 0
while True:
    MyNumber = input("Please enter a number: ")
    try:
        valid_number = int(MyNumber)
        break
    except ValueError:
        print("Seriously, don't you read the instructions. \nI asked for a number...")
        count += 1
print(valid_number)
print("You have made",count,"errors.")
