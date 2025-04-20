FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-300,260)
        self.score = 1
        self.hideturtle()
        self.write(F"Level {self.score}",align="left",font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(F"Level {self.score}", align="left", font=FONT)

    def increment(self):
        self.score +=1
        self.update_scoreboard()

    def game_over(self):
        self.goto(-80,0)
        self.write("GAME OVER", align="left", font=FONT)
