"""
GC12	35	BROTHERLY SCREENTIME
Sadly there is only one PS4 in the house and so the children always argue as to how much time they get. Make a timer that givens an equal amount of time for each sibling.
"""

#Get the number of children.
children = int(input("How many children do you have?: "))

#Get hour/minutes of screentime.
hours = int(input("How many hours?: "))
minutes = int(input("How many minutes?: "))

#Calculate total miinutes, and divide by number of children to get time per child.
total_minutes = (hours*60) + minutes
time_per_child = total_minutes//children

#Get the time the person starts playing.
time = input("What is the time now?")
hour_min = time.split(':')

#Get the hour/minute.
hour = int(hour_min[0])
minute = int(hour_min[1])

#Iterate over the number of children where the playing time would be calculated and outputted to the user.
for i in range(children):
    if minute < 10:
        print("The children number,",i+1,"will start playing at: " + str(hour) + ':'+'0'+str(minute)) 
    else:
        print("The children number,",i+1,"will start playing at: " + str(hour) + ':'+str(minute))
    minute += time_per_child
    #Check if the minute number exceeds 60 (add one hour/deduct 60 from minutes).
    if minute >= 60:
        hour += 1
        minute  -= 60
