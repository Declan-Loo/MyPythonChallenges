"""
GC09	40	99 BOTTLES OF COLA	
99 bottles of cola on the wall. 99 bottles of cola, take one down, pass it around. 98 bottles of cola on the wall. 98 bottles of cola, take one down, pass it around.... A computer should be able to sing this song in no time at all...    
"""
#While loop to print the lyrics with the number of cola decrementing.
for bottle_no in range(99,1,-1):
    #Print the lyrics.
    print(bottle_no,"bottles of cola on the wall.")
    print(bottle_no,"bottles of cola, take one down, pass it around.")

#Print the lyrics for one bottle/no more bottles (I found the lyrics for that on the internet to complete the song).
print("1 bottle of cola on the wall.")
print("1 bottle of cola, take one down, pass it around.")
print("No more bottles of cola on the wall.")
print("Go to the store and buy some more.")
