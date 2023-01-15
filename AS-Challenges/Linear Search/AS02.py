"""
AS02	
100	
LINEAR SEARCH	
Write the Python required to do a linear search of Python in an array	
"""

from random import shuffle

#Initialise empty list
ret = []

#Add numbers into the array
for i in range(1,101):
  #Array is from 1 to 100
  ret.append(i)


#Shuffle the array in a random order :-)
shuffle(ret)

#Set found to False
found = False

#Makes sure only integers are inputted.
try:
  #Prompt user for number to be found
  number = int(input('Number: '))

  #Iterates through the l
  for i in range(len(ret)):
    #During iteration, check if the element matches the number
    if ret[i] == number:
      #Print out the position of the number in the array and the number
      print(f"Found it! \nNumber: {number} \nPosition: {i+1}")

      #Re-assign found to be True
      found = True

  #If the number is not found in the array after iteration, print Not Found
  if found == False:
    print("Not found!")
except:
  # Remind the user to only input numbers, not any other data types eg bool,str,char.
  print("NUMBERS ONLY, NOT CHARACTERS")
