"""
AS25	
50	
HISTOGRAMS	

Define a procedure histogram that takes a list of integers and prints a histogram to the screen. For example, histogram([4, 9, 7]) should print the following:
****
*********
*******
"""

def histogram(list_for_histogram):
  LoopCounter = len(list_for_histogram)
  for i in range(LoopCounter):
    print("*" * list_for_histogram[i])

histogram([4,9,7])
