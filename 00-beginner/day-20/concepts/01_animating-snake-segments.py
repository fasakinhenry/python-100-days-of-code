# import turtle
from turtle import Turtle, Screen
import time

# Setup the screen with custom properties
screen = Screen()
screen.bgcolor("black")
screen.title("My snake Game")
screen.tracer(0)
screen.setup(width=600, height=600)

# create a snake array to hold the squares that makes up the snake
# snake = []
initial_position = 0

# Create an array segments to hold all the segments of the snake
segments = []

for position in range(3):
    new_turtle = Turtle("square")
    new_turtle.setx(initial_position)
    new_turtle.color("white")
    new_turtle.penup()
    offset = initial_position + (position * -20)
    new_turtle.setx(offset)
    segments.append(new_turtle)

game_is_on = True
# The game loop to automate movement of the snake
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    
    segments[0].forward(20)

screen.exitonclick()
