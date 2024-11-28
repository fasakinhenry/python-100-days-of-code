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
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=("Calibri", 24, "normal"))
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

