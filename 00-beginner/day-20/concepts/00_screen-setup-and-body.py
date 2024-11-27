# import turtle
from turtle import Turtle, Screen

# Setup the screen with custom properties
screen = Screen()
screen.bgcolor("black")
screen.title("My snake Game")
screen.setup(width=600, height=600)

# create a snake array to hold the squares that makes up the snake
# snake = []
initial_position = 0
print(initial_position)

for position in range(3):
    new_turtle = Turtle("square")
    new_turtle.setx(initial_position)
    new_turtle.color("white")
    offset = initial_position + (position * -20)
    new_turtle.setx(offset)

screen.exitonclick()
