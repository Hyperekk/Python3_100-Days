from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from snake import Snake
import time

screen = Screen() 
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key = "Up", fun=snake.up)
screen.onkey(key = "Down", fun=snake.down)
screen.onkey(key = "Left", fun=snake.left)
screen.onkey(key = "Right", fun=snake.right)


game_on = True

while game_on:
    time.sleep(0.07)
    screen.update()
    snake.move()
    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.new_food()
        scoreboard.increase()
        snake.extend()
    
    #Collision with walls
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    #Collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

    


        



























screen.exitonclick()