from turtle import Turtle

# Create constants to be used
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

# create a scoreboard class that inherits from the Turtle class
class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.high_score = self.reset_high_score()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.sety(265)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def read_high_score(self):
        with open("C:/Users/HP/Desktop/python-100-days-of-code/00-beginner/day-24/exercises/00_snake/data.txt") as file:
            return file.read()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

