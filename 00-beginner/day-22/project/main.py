from turtle import Screen

# create an object of the screen class
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game - Famous arcade game")

# Ensure screen exits when it is clicked
screen.exitonclick()
