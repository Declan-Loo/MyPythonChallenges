"""
AS79	
60	
MAKE IT LAUGH PROCEDURE	
Write a procedure make_it_laugh(string) to replace all vowels in an input string with "haha". Print the modified string after to verify your procedure has worked.
"""

def make_it_laugh(string):
  letters = list(string)
  for i in range(0,len(letters)):
    if letters[i] in ['a','e','i','o','u']:
      letters[i] = "haha"
  string = "".join(letters)
  print(string)

sentence = input("Sentence: ")
make_it_laugh(sentence)
