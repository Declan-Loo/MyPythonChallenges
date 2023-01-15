"""
AS24	
50	
PROJECT TIMELINE	
Create a program to calculate the number of days a project is based on two dates entered. The project might be anything from 1 day to more than 1 year in length. (Use of datetime library encouraged.)	
"""

from datetime import *
try:
  # Date1
  Date1 = int(input("Date 1: "))
  Month1 = int(input("Month 1: "))
  Year1 = int(input("Year 1: "))
  dmy1 = date(Year1, Month1, Date1)

  # Date2
  Date2 = int(input("Date 2: "))
  Month2 = int(input("Month 2: "))
  Year2 = int(input("Year 2: "))
  dmy2 = date(Year2, Month2, Date2)

  print(dmy1)
  print(dmy2) 
  difference = dmy2 - dmy1
  print(difference)

except:
  print("Invalid date")
