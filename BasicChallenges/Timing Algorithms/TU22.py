"""
TU22	
40	
TIMING ALGORITHMS	
Learn how to time the speed of your algorithms
"""

import datetime

def timed_proc():
  while True:
    answer = input("Enter: ")
    if answer == "the lazy fox jumped over the brown dog":
      break

start_time = datetime.datetime.now()  # Starts the timer, by putting the time into start_time variable
timed_proc()  # Whatever you want to time
time_taken = datetime.datetime.now()-start_time  # Current time - start time
print(time_taken)  # Printing the time it took
