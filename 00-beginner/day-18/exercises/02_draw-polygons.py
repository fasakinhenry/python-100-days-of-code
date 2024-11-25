# import the turtle and screen class
from turtle import Turtle, Screen
import random

# Create a turtle colors array
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

turtle = Turtle()

# Create a loop to draw the polygons
for deg in range(3, 11):
    for move in range(deg):
        turtle.forward(100)
        turtle.right(360/deg)
    # change the color of the pen after each shape
    turtle.color(random.choice(colors))


screen = Screen()
screen.exitonclick()
