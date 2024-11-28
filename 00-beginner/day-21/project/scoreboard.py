from turtle import Turtle

# create a scoreboard class that inherits from the Turtle class
class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.sety(265)
        self.write(f"Score: {self.score}", align="center", font=("Calibri", 24, "normal"))
