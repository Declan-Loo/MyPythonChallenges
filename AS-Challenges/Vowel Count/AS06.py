"""
AS06	
50	
VOWEL COUNT	
How many vowels does a word have? You are going to find out...	
"""

word = input("Word: ")
no_of_characters = len(word)
vowel_count = 0
for i in range(no_of_characters):
  if word[i] in ['a','e','i','o','u']:
    vowel_count += 1

print("Vowels in word:",vowel_count)
