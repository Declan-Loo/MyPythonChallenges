"""
GC04	
35	
MARIO PYRAMID	

User inputs a number. It then creates the appropriate sized pyramid. e.g. Pyramid Size 3
x
xxx
xxxxx
"""

number = int(input("Number: "))
for i in range(1,number+1):
  print(i * "*")
