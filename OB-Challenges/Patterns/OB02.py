"""
You have been given a Turtle pattern generator and a file with common patterns. However, the original programmer hasn't worked out how to connect the two. You have been asked to import the file and make it create the patterns the five patterns. The first line is the angle and then the second line is the number of times to execute it. 
"""

import turtle


class pattern():
    def __init__(self, angle: int, times: int):
        self.__angle = angle # Integer
        self.__times = times # Integer

    def draw_pattern(self):
        colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
        turtle.setup(800, 600)  # setting window dimensions
        turtle.bgcolor('black')
        for x in range(self.__times):
            turtle.pencolor(colors[x % 6])
            turtle.width(x / 100 + 1)
            turtle.forward(x)
            turtle.left(self.__angle)
        turtle.done()

pattern_list = []

with open('patterns.txt', 'r') as f:
    num_lines = len(f.readlines()) #Counts lines
    f.seek(0) #Puts back to first position
    
    for i in range(num_lines//2):
        angle = int(f.readline())
        times = int(f.readline())
        pattern_list.append(pattern(angle,times))
        
for pattern in pattern_list:
    pattern.draw_pattern()
    
