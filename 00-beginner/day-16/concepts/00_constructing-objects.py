# Get started with the Turtle class
from turtle import Turtle, Screen

# Create a new object from the turtle class
timmy = Turtle()

# Print the new created turtle object
print(timmy)
# Change the shape of the turtle object
timmy.shape("turtle")
# Change the color of the turtle object
timmy.color("coral")

# Move the turtle forward by 100 paces
timmy.forward(100)

# Create a new screen object
my_screen = Screen()

# Print the canvas height of the screen
print(my_screen.canvheight)

# Show up screen until it is clicked
my_screen.exitonclick()
