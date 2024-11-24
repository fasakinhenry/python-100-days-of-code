# import the turtle and screen class
from turtle import Turtle, Screen

turtle = Turtle()

# Create a loop to draw the polygons
for deg in range(3, 10):
    for move in range(deg):
        turtle.forward(100)
        turtle.right(360/deg)


screen = Screen()
screen.exitonclick()
