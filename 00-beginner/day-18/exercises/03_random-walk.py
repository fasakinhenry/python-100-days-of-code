# Implement the turtle Random Walk
from turtle import Turtle, Screen
import random

turtle = Turtle()

# create the colors array
colors = ["cornflower blue", "dark orchid", "indian red", "deep sky blue", "light sea green", "wheat", "slate gray", "sea green"]

# Implement the turtle Random Walk
turtle.speed("fastest")

for _ in range(200):
    turtle.setheading(random.choice([0, 90, 180, 270]))
    turtle.color(random.choice(colors))
    turtle.pensize(10)
    turtle.forward(30)

screen = Screen()
screen.exitonclick()
