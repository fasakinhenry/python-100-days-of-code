# import turtle
from turtle import Turtle

# Create an array segments to hold all the segments of the snake

STARTING_POSITION = 0
MOVE_DISTANCE = 20

class Snake:
    def __init__(self) -> None:
        self.segments = []
        self.color = "white"
        self.initial_position = STARTING_POSITION
        self.create_snake()
    
    def create_snake(self):
        for position in range(3):
            new_turtle = Turtle("square")
            new_turtle.setx(self.initial_position)
            new_turtle.color(self.color)
            new_turtle.penup()
            offset = self.initial_position + (position * -20)
            new_turtle.setx(offset)
            self.segments.append(new_turtle)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.segments[0].forward(MOVE_DISTANCE)
    
    def up(self):
        self.segments[0].setheading(90)

    def down(self):
        self.segments[0].setheading(270)

    def left(self):
        self.segments[0].setheading(180)

    def right(self):
        self.segments[0].setheading(0)


