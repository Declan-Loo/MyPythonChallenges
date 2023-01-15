"""
TT04	
25	
ANY SHAPE	
Use turtle so that when you enter a number it creates a polygon with that many sides.	
"""

"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle

t = turtle.Turtle()

x = int(input("Number of sides? "))

t.circle(100,360,x)
