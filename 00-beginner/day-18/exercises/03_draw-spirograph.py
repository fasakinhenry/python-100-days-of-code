# Draw spirograph
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

turtle.speed("fastest")

for _ in range(72):
    turtle.color(random_color())
    turtle.circle(100)
    turtle.setheading(turtle.heading() + 5)


screen = t.Screen()
screen.exitonclick()
