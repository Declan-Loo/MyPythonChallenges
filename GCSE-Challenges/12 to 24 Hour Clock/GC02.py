"""
GC02	
25	
12 TO 24 HOUR CLOCK	
User inputs 12 hour clock and am or pm and you will convert it to the 24 hour equivalent.
"""

Clock = int(input("Hour: "))
Minute = int(input("Minute: "))
AMPM = input("AM or PM? ")

if AMPM in ['AM','am']:
  print(str(Clock) + ":" + str(Minute))
else:
  print(str(Clock+12) + ":" + str(Minute))
