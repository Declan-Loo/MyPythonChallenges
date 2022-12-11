"""
CODE: TU03 POINTS: 10
HOW TO PRINT MIXED STRINGS AND NUMBERS
"""
MyAge = int(input('What is your age?'))

#Exercise 1: Tell the person that MyAge "Is a very nice age to be"
print('%d is a very nice age to be' % MyAge)

#Exercise 2: Change the code so that the computer has an age to 3 decimal places and is older than you.
ComputerAge=3.453
MyAge = int(input('What is your age?'))
print('I am older than %d, because I am %.3f' % (MyAge,ComputerAge))
