# import turtle
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# Setup the screen with custom properties
screen = Screen()
screen.bgcolor("black")
screen.title("My snake Game")
screen.tracer(0)
screen.setup(width=600, height=600)

snake = Snake()
food = Food()
score_board = ScoreBoard()

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
        snake.extend()
        score_board.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -310 or snake.head.ycor() > 310 or snake.head.ycor() < -280 :
        score_board.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score_board.reset()
            snake.reset()

screen.exitonclick()
