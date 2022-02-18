from turtle import Turtle, Screen, colormode
import random

bob = Turtle()
bob.shape("turtle")
bob.color("red")

colormode(255)

def random_color():
    r = random.randint (0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r,g,b)
    return colour

bob.speed("fastest")
bob.width(2)

for i in range(0,365,5):
    bob.color(random_color())
    bob.circle(100)
    bob.setheading(i)


# ----- FIGURY -----

# def draw_shape(side):
#     for i in range(side):
#         bob.fd(100)
#         bob.left(360/side)

# for i in range(3,11):
#     draw_shape(i)
#     bob.color(random_color())

#-------RANDOM WALKER-------
# bob.pensize(10)
# bob.speed(20)
# for i in range(500):
#     num = random.randint(1,4)
#     bob.color(random_color())
#     if num == 1:
#         bob.fd(20)
#     elif num == 2:
#         bob.bk(20)
#     elif num == 3:
#         bob.left(90)
#         bob.fd(20)
#     else:
#         bob.right(90)
#         bob.fd(20)

screen = Screen()
screen.exitonclick()