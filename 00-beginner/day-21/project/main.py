# import turtle
from turtle import Screen
from snake import Snake
from food import Food
import time

# Setup the screen with custom properties
screen = Screen()
screen.bgcolor("black")
screen.title("My snake Game")
screen.tracer(0)
screen.setup(width=600, height=600)

snake = Snake()
food = Food()

# add Event listeners to handle snake movement
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
# The game loop to automate movement of the snake
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision of snake with food
    if snake.head.distance(food) < 15:
        food.refresh()

screen.exitonclick()
