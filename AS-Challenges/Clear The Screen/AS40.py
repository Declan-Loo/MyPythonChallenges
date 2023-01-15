"""
AS40	
50	
CLEAR THE SCREEN	
Unlike most languages there isn't a Clear Screen procedure in Python. Can you make one?	
"""

#Clear screen by printing 100 new lines
def csl():
  print("\n"*100)

while True:
  x = input()
  if x == "":
    break
  choice = input("Clear screen? ")
  if choice == "yes":
    csl()
  else:
    print(x)
  
