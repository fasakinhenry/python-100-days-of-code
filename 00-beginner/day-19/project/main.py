from turtle import Turtle, Screen
import random

# create the Screen object
screen = Screen()

# set the screen title
screen.title("Turtle Racing game")

# Set the width and height of the screen
screen.setup(width=500, height=400)

# Set the variable to handle the game loop
is_race_on = False

# create a colors array to store the colors of each turtle
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# create the y position array to store the y position of each turtle
y_positions = [-70, -40, -10, 20, 50, 80, 110]

# Create a array to hold all the turtle players
all_turtles = []

# Ask for user input to bet on a turtle
user_bet = screen.textinput(
    title="Make your bet",
    prompt="Which turtle will win, enter a color: "
)

# create the turtle objects
for turtle_position in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_position])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_position])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
