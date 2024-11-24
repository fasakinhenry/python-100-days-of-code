# import the turtle and screen class
from turtle import Turtle, Screen

turtle = Turtle()

# Create a loop to draw the dashed line
for _ in range(15):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()


screen = Screen()
screen.exitonclick()
