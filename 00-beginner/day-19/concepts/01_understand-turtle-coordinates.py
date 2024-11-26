from turtle import Turtle, Screen

# create the Screen object
screen = Screen()

# set the screen title
screen.title("Turtle Racing game")

# Set the width and height of the screen
screen.setup(width=500, height=400)

# create a colors array to store the colors of each turtle
colors = ["red", "blue", "green", "yellow", "orange", "purple", "violet"]

# create the y position array to store the y position of each turtle
y_positions = [-70, -40, -10, 20, 50, 80, 110]

# Ask for user input to bet on a turtle
user_bet = screen.textinput(
    title="Make your bet",
    prompt="Which turtle will win, enter a color: "
)

# create the turtle objects
for turtle_position in range(0, 7):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[turtle_position])
    turtle.penup()
    turtle.goto(x=-230, y=y_positions[turtle_position])


screen.exitonclick()
