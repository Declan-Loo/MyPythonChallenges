"""
AS14	50	
BRACKETS CHECKER	
Create a program to make sure that the number of brackets is balanced.	
"""

#Function to check brackets is balanced or not.
def is_balanced(string):
    #Initialise Bracket Count
    bracket_count = 0
    #Iterate for character in string
    for char in string:
        #Check open bracket
        if char == '(':
            #Increment if open bracket present
            bracket_count += 1
        #Check closed bracket
        elif char == ')':
            #Decrement count if closed bracket is present
            bracket_count -= 1
    #Check if balanced and output appropriate message.
    if bracket_count == 0:
        return "The number of brackets is balanced"
    else:
        return "The number of brackets is not balanced"
        
# Test the function
test_cases = [
    "()",
    "((()))",
    "(((()))",
    "(()))",
    "(()())(",
]

for i in test_cases:
    print(i)
    print(is_balanced(i))
    print()
