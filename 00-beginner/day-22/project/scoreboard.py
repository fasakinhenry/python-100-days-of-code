from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(-100, 180)
        self.write(self.l_score, align="center", font=("Poppins", 80, "normal"))
        self.goto(100, 180)
        self.write(self.r_score, align="center", font=("Poppins", 80, "normal"))
