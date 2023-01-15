"""
GC39
50	
STUDENT CREATED: THE ROASTING MACHINE	
The Random Insult Generator. You have horrible comebacks, and just keep on getting roasted by everyone. This code will help you take your revenge. It must ask for the student’s name, and include that when roasting. There must be a random generator based upon a list.	
"""

from random import randint
insult_list = ['Jealousy is a disease. Get well soon.',
               'You don’t like me? That’s a shame. I’ll pencil in some time to cry about it later. Right now, I’m busy enjoying my life.',
               'I’m an acquired taste. Don’t like me, acquire some taste.','Do you always act like an ***** or do you just show off when I’m around?',
               'Grab a straw because you suck.',
               'I don’t hate you but let’s put it this way…, if I had a bucket of water and you were on fire, I’d drink the water.',
               'Some call them haters, I call them motivators.','If I wanted to listen to an ***hole I’d fart.','Haters gonna hate.',
               'Acting like a **** won’t make yours any bigger.']
name = input("Name of person: ")

print(name + ",",insult_list[randint(0,9)])

#alternatively can do random.choice(insult_list)
