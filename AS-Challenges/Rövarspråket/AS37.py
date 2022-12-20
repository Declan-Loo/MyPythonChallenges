"""
AS37	100	
Rövarspråket	

STUDENT SUBMITTED: This is a SUPER-SECRET language. Rövarspråket is not very complicated: you take an ordinary word and replace the consonants with the consonant doubled and with an "o" in between. So the consonant "b" is replaced by "bob", "r" is replaced with "ror", "s" is replaced with "sos", and so on. Vowels are left intact. It's made for Swedish, but it works just as well in English.	
"""

#Get word input from user.
word = input("Word?: ")

#Initialise empty string variable.
final_word = ''

#Loop over letters in word.
for letter in word:
    #Check if letter is vowel.
    if letter in ['a','e','i','o','u']:
        #Add letter as vowels are left intact.
        final_word += letter
    else:
        #Add (letter+'o'+letter) to final_word.
        final_word += (letter + 'o' + letter)

#Print the final word converted to Rovarspraket.
print("Word in Rovarspraket: " + final_word)
