from turtle import Turtle, Screen, colormode
import random

screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make Your Bet",prompt="Enter color which you think will win: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_index = []

turtle_y = -100
for i in range(6):
    mike = Turtle()
    mike.shape("turtle")
    mike.color(colors[i])
    mike.penup()
    mike.speed("fastest")
    mike.goto(x=-230, y=turtle_y)
    turtle_y += 40
    turtle_index.append(mike)

if bet:
    is_on = True

while is_on:
    for turtle in turtle_index:
        if turtle.xcor() > 230:
            win_col = turtle.pencolor()
            if win_col == bet.lower():
                print("You've won!")
            else:
                print("You've lost!")
            is_on = False
        else:
            distance = random.randint(0,30)
            turtle.forward(distance)

screen.exitonclick()