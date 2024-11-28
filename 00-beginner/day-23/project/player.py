from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.starting_position = STARTING_POSITION
        self.penup()
        self.goto(self.starting_position)
        self.setheading(90)

    def move(self):
        self.new_y = self.ycor() + 20
        self.goto(self.xcor(), self.new_y)
