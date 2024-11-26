# Implement the turtle Random Walk
import turtle as t
import random

turtle = t.Turtle()

# Change the color mode using the turtle class
t.colormode(255)

# create function to generate random colors
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)

# create the colors array
# colors = ["cornflower blue", "dark orchid", "indian red", "deep sky blue", "light sea green", "wheat", "slate gray", "sea green"]
directions = [0, 90, 180, 270]
turtle.speed("fastest")

for _ in range(200):
    turtle.setheading(random.choice(directions))
    # turtle.color(random.choice(colors))
    turtle.color(random_color())
    turtle.pensize(10)
    turtle.forward(30)

screen = t.Screen()
screen.exitonclick()
