"""
GC10	
40	
THE EVIL MATHS TEACHER	
An evil maths teacher has locked his students in school until they manage to type the first 100 numbers of the Fibonacci sequence. Can you think of a quicker way to do it in Python?	
"""

def fibonacci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

for i in range(100):
    print(fibonacci(i))
