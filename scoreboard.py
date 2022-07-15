from turtle import Turtle
import score as sco
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high = sco.high_score
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
    def update(self):
        self.clear()
        self.color('white')
        self.write(f"score is {self.score} High Score: {self.high}", align="center", font=('Arial', 32, "normal"))
    def update1(self):
        self.score += 1
        c = Scoreboard()
        c.update()
        self.color('black')
        self.clear()
        self.update()
    def reset(self):
        if self.score > self.high:
            self.high = self.score
        self.score = 0
        self.color('black')
        self.clear()
        self.update()
    def update_score1(self):
        sc = open("score.py", "w")
        sc.write(f"high_score = {self.high}")
