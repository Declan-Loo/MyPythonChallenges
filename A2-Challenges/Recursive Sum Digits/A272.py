"""
A272	
100	
RECURSIVE SUM DIGITS	
Write a recursive program to get the sum of each digit in an integer. e.g. sumDigits(345) -> 12 or sumDigits(45) -> 9
"""

def number(n):
    if n == 0:
        return 0
    else:
        return n % 10 + number(n//10)

print(number(1052))
