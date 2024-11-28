from turtle import Turtle

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        self.new_x = self.xcor() + self.x_move
        self.new_y = self.ycor() + self.y_move
        self.goto(self.new_x, self.new_y)
        self.bounce()
    
    def bounce(self):
        if self.ycor() > 280 or self.ycor() > 280:
            self.y_move *= -1
