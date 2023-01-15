"""
AS82	
50	
STRING REVERSAL FUNCTION	
Create a function that returns the reverse of a string	
"""

def string_reversal(string):
  string_length = len(string)
  for i in range(-1,-string_length-1,-1):
    print(string[i],end="")



string_input = input("Enter string here: ")
string_reversal(string_input)
print()
