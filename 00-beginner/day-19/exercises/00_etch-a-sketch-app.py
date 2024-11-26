from turtle import Turtle, Screen

# create the turtle object
tim = Turtle()

# create a function to move the turtle forwards
def move_forwards():
    tim.forward(10)

# create a function to move the turtle backwards
def move_backwards():
    tim.backward(10)

# create a function to move the turtle left
def turn_left():
    tim.left(10)

# create a function to move the turtle right
def turn_right():
    tim.right(10)

# Create a function to clear the screen after drawing
def clear():
    tim.clear()
    tim.penup()
    tim.home()


# Create the Screen object
screen = Screen()
screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
