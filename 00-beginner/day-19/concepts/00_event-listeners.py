from turtle import Turtle, Screen

# create the turtle object
tim = Turtle()

# create a function to move the turtle forwards
def move_forwards():
    tim.forward(10)


# Create the Screen object
screen = Screen()
screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()
