from turtle import Turtle
import time
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 3
        self.y_move = 3

    def move(self):
        
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bounce(self):
        self.y_move *= -1

    def bouncex(self):
        self.x_move *= -1

    def reset(self):
        self.home()
        self.bouncex()
        time.sleep(1)

    def speed_up(self):
        self.x_move += 2
        self.y_move += 2
