"""
A272
100
GREATEST COMMON DIVISOR	
In mathematics, the greatest common divisor (GCD) of two or more integers, which are not all zero, is the largest positive integer that divides each of the integers. Create a recursive program to find the greatest common divisor.	
"""

# Function to get Greatest Common Divisor
def gcd(a,b):
    #Base Case
    if b == 0:
        return a
    else:
        #Recursive Function
        return gcd(b, a%b)
#Print GCD of 57 and 2103021
print(gcd(57,2103021))
