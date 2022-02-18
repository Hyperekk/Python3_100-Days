from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-290,260)
        self.level = 1
        self.write(f"Level: {self.level}",font=FONT)

    def update(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}",font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",font=FONT,align="center")
