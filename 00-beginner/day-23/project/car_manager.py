from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self) -> None:
        super().__init__()
        self.cars = []
        
    
    def create_car(self):
        # Create cars less frequently
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(1, 2)
            self.new_y = random.randint(-250, 250)
            new_car.goto(300, self.new_y)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def level_up(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT

    
    # Method to add new cars
    # Method to remove new car


