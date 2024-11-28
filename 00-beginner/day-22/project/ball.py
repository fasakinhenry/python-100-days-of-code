from turtle import Turtle

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):
        self.new_x = self.xcor() + 10
        self.new_y = self.ycor() + 10
        self.goto(self.new_x, self.new_y)
