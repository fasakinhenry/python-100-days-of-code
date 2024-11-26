# import turtle
from turtle import Screen
from snake import Snake
import time

# Setup the screen with custom properties
screen = Screen()
screen.bgcolor("black")
screen.title("My snake Game")
screen.tracer(0)
screen.setup(width=600, height=600)

snake = Snake()

game_is_on = True
# The game loop to automate movement of the snake
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()

screen.exitonclick()
