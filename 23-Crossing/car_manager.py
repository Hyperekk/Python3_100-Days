from turtle import Turtle
import random
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self) -> None:
       self.cars = []
       self.speed = STARTING_MOVE_DISTANCE

    def create(self):
        i = random.randint(1,6)
        if i >= 6:
            global car
            car = Turtle()
            car.shape("square")
            car.penup()
            car.shapesize(1,2)
            car.color(random.choice(COLORS))
            car.goto(x=300,y=random.randint(-250,250))
            car.setheading(180)
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.forward(self.speed)

    def faster(self):
        self.speed += MOVE_INCREMENT



