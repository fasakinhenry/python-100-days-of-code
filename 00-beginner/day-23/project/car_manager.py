from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.cars = []
        self.shape("square")
        self.penup()
        self.color(random.choice(COLORS))
        self.new_y = random.randint(-250, 250)
        self.goto(self.xcor(), self.new_y)
    
    def move(self):
        pass
    # Method to add new cars
    # Method to remove new car


