# import turtle
from turtle import Turtle, Screen
import time

# Create an array segments to hold all the segments of the snake
segments = []
initial_position = 0

class Snake:
    def __init__(self) -> None:
        pass

    def forward(self):
        for seg_num in range(len(segments) - 1, 0, -1):
            new_x = segments[seg_num - 1].xcor()
            new_y = segments[seg_num - 1].ycor()
            segments[seg_num].goto(new_x, new_y)

for position in range(3):
    new_turtle = Turtle("square")
    new_turtle.setx(initial_position)
    new_turtle.color("white")
    new_turtle.penup()
    offset = initial_position + (position * -20)
    new_turtle.setx(offset)
    segments.append(new_turtle)

