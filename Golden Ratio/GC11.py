"""
GC11	30	GOLDEN RATIO
A painter wants to know what size to make his paintings, she's heard of this golden ratio, but doesn't know how to calculate it. Given a length can you calculate the height for a landscape.
"""

#The golden ratio.
golden_ratio = 1.618

#Get the input of the landscape from the user.
landscape = float(input("Landscape length?: "))

#Calculate the height of the painting.
height = landscape / golden_ratio

#Output the height to the user.
print("The height needed for your painting is: " + str(height))
