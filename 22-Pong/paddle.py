from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,cord) -> None:
        super().__init__()
        x = cord[0]
        y = cord[1]
        self.shape("square")
        self.speed("fastest")
        self.penup()
        self.turtlesize(5,1)
        self.speed()
        self.color("white")
        self.goto(x,y)

    def move_up(self):
        new_y = self.ycor()+20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor()-20
        self.goto(self.xcor(), new_y)