from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1

    def write_score(self):
        self.penup()
        self.goto(-270, 240)
        self.hideturtle()
        self.color("black")
        self.write(f"Level: {self.level}", font=FONT)

    def score_increase(self):
        self.clear()
        self.level += 1

    def game_over(self):
        over = Turtle()
        over.hideturtle()
        over.penup()
        over.color("black")
        over.write("Game Over", align="center", font=FONT)
