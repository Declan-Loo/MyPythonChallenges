"""
A266	
75	
BIG O DISPLAY	
Create a chart system to show common Big O algorithm growth types.
"""

#Import matplotlib
import matplotlib.pyplot as plt
import math

plt.style.use('ggplot')

#Smaller range as bigger range will make graph hard to see as too big number for exponent.
x = [i for i in range(0,5)]
y_log = [math.log(i) for i in range(1,6)]
y_exponent = [2**i for i in range(1,6)]
y_factorial = [math.factorial(i) for i in range(1,6)]
y_quadratic = [math.sqrt(i) for i in range(1,6)]

plt.plot(x, y_log,'b',label='Logarithm graph')
plt.plot(x, y_exponent,'r',label='Exponential graph')
plt.plot(x, y_factorial,'y',label='Factorial graph')
plt.plot(x, y_quadratic,'g',label='Quadratic graph')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.show()
