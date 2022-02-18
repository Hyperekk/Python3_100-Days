from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.L_score = 0
        self.R_score = 0
        
    def update(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.L_score, align="center", font=("Courier",80,"normal"))
        self.goto(100,200)
        self.write(self.R_score, align="center", font=("Courier",80,"normal"))

    def add_L(self):
        self.L_score += 1
        self.update()

    def add_R(self):
        self.R_score += 1
        self.update()