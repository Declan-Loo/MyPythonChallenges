"""
OB01	100
DAD JOKES
Create Dad Joke Objects in this hilarious challenge! (See Extra Info for full details)	
https://www.google.com/url?q=https://docs.google.com/presentation/d/1JjeVtxjFna4KyUYZrb0_S3CxWMWhM6EijmSRWMSNtdU/edit%23slide%3Did.p1&sa=D&source=editors&ust=1672163381939898&usg=AOvVaw26KGL4OBzu-ANYxh46LJjx
"""

import random
import time
import os
class DadJokes:
    def __init__(self,prompt,answer):
        self.__prompt = prompt #The joke starter or question
        self.__answer = answer #The joke reply/answer
    
    def PrintRandomJoke(self): #It prints a random Prompt, then prompts the user for an answer and then reveals the actual answer
        print(self.__prompt)
        answer = input("Answer: ")
        time.sleep(5)
        print(self.__answer)

textfile = 'DadJokes.txt'

jokes_list = []

try:
    with open(textfile, 'r') as f:
        Lengthoffile = len(f.readlines())
        print(Lengthoffile)
        
    with open(textfile, 'r') as f:
        for i in range(Lengthoffile//2):
            prompt = f.readline().strip()
            answer = f.readline().strip()
            jokes_list.append(DadJokes(prompt,answer))
    
except IOError:
    print("File not found. Your directory is",os.getcwd())
    
random.choice(jokes_list).PrintRandomJoke()


