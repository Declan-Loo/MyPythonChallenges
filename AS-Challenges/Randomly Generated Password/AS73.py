"""
AS73	150
RANDOMLY GENERATED PASSWORD	
Can you create a randomly generated password based off a favorite color, place and animal? And also add special characters to the end of it.
"""
import random

#initalise variaible to store password.
generated_password = ""

#Generate list of special characters using ASCII characters.
special_characters = [chr(x) for x in range(33,48)]

#Get input for favorite color, place and animal from user.
favourite_colour = input("What is your favourite colour?: ")
favourite_place = input("What is your favourite place?: ")
favourite_animal = input("What is your favourite animal?: ")

#Randomise order to put these 3 variables for password generation.
randomizer = []
randomizer.append(favourite_colour)
randomizer.append(favourite_place)
randomizer.append(favourite_animal)

choice1 = random.choice(randomizer)
randomizer.remove(choice1)
choice2 = random.choice(randomizer)
randomizer.remove(choice2)
choice3 = random.choice(randomizer)

#Randomise number of occurances of random characters for each side.
no_of_random_characters1 = random.randint(1,5)
no_of_random_characters2 = random.randint(1,5)

#Add the first set of random characters.
for i in range(no_of_random_characters1):
    generated_password += random.choice(special_characters)
    
#Add the randomised order with capitalisation, upper case and numbers to make stronger password.
generated_password += choice1
generated_password += choice2.capitalize()
generated_password += choice3.upper()
generated_password += random.randint(1,1032131)

#Append the last set of random characters.
for i in range(no_of_random_characters2):
    generated_password += random.choice(special_characters)
    
#Print the generated password.
print("Your generated password is:",generated_password)
