"""
TU07	
12	
SIMPLE LOOP	
Using a FOR loop
"""

"""
for i in range (1,100):
    print(i)

Exercise 1: Why does it only count to 99? Adjust the code to count and print to 100.
"""

for i in range(1,101):
  print(i)

"""
for i in range (1,100,2):
​    print(i)

Exercise 2: Count the even numbers between 0 & 100.
"""
for i in range(0,101,2):
  print(i)

"""
for i in range (100,0,-1):
    print(i)

There are a few ways to do this, but the easiest is to start with the top number, then the bottom number followed by the step. 

Exercise 3: Try counting down in steps of 10 from 1,000
"""

for i in range(1000,0,-10):
  print(i)
