from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600, startx=350)
screen.title("Pong")
screen.tracer(0)

paddle = Paddle((350,0))
paddle2 = Paddle((-350,0))

ball = Ball()

scoreboard = Scoreboard()
scoreboard.update()

screen.listen()
screen.onkeypress(paddle.move_up,"i")
screen.onkeypress(paddle.move_down,"k")
screen.onkeypress(paddle2.move_up,"w")
screen.onkeypress(paddle2.move_down,"s")

game_on = True

while game_on:
        screen.update()
        time.sleep(0.01)
        ball.move()

        #Collision with Y
        if ball.ycor() > 285 or ball.ycor() < -285:
                ball.bounce()

        #Collision with paddle
        if (ball.distance(paddle) <= 50 and (ball.xcor() >= 330 and ball.xcor() < 340)) or (ball.distance(paddle2) <= 50 and (ball.xcor() <= -330 and ball.xcor() > -340)):
                ball.bouncex()

        if ball.xcor() >= 400: 
                ball.reset()
                scoreboard.add_L()
        
        if ball.xcor() <= -400:
                ball.reset()
                scoreboard.add_R()


screen.exitonclick()