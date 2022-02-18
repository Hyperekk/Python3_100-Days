from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.goto(x = 0, y = 280)
        self.pencolor("white")
        self.score = 0
        with open("data.txt",mode="r") as f:
            self.highscore = int(f.read())
        self.write(arg = f"Score = {self.score}, Highscore = {self.highscore}", align="center", font = ('Arial',12,'normal'))

    def increase(self):
        self.clear()
        self.goto(x = 0, y = 280)
        self.score += 1
        self.write(arg = f"Score = {self.score}, Highscore = {self.highscore}", align="center", font = ('Arial',12,'normal'))

    def reset(self):
        if self.score > self.highscore:
            with open("data.txt",mode="w") as f:
                self.highscore = self.score
                f.write(f"{self.highscore}")
        self.score = 0
        self.clear()
        self.goto(x = 0, y = 280)
        self.write(arg = f"Score = {self.score}, Highscore = {self.highscore}", align="center", font = ('Arial',12,'normal'))