import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(fun= player.move, key="w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    manager.create()
    manager.move()
    for car in manager.cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.check_finish_line():
        player.reset()
        manager.faster()
        scoreboard.update()

    screen.update()

screen.exitonclick()
