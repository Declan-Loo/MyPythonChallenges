"""
TT09	
25	
THE MAZE (EASY EDITION)	
Have fun solving our little maze!
"""

import turtle
turtle.color("red")
turtle.begin_fill()
for i in range (4):
    turtle.forward(50)
    turtle.right(90)
turtle.end_fill()

turtle.penup()
turtle.goto(-200,200)
turtle.color("blue")
turtle.pendown()
turtle.begin_fill()
for i in range(5):
  turtle.forward(50)
  turtle.right(72)
turtle.end_fill()
turtle.penup()
turtle.goto(200,100)
turtle.color("magenta")
turtle.pendown()
turtle.begin_fill()
for i in range(6):
  turtle.forward(50)
  turtle.right(60)
turtle.end_fill()
