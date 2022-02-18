# import colorgram

# colors = colorgram.extract("image.jpg",22)
# rgb_col = []
# for color in colors:
#     R = color.rgb.r
#     G = color.rgb.g
#     B = color.rgb.b
#     new_color = (R,G,B)
#     rgb_col.append(new_color)
# print(rgb_col)
from turtle import Turtle,Screen,colormode
import random
colormode(255)
bob = Turtle()
bob.speed("fastest")
bob.hideturtle()
colors = [
    (236, 35, 108), (221, 232, 237), (145, 28, 64), (239, 75, 35), (6, 148, 93), (232, 238, 234), (231, 168, 40), 
    (184, 158, 46), (44, 191, 233), (27, 127, 195), (126, 193, 74), (253, 223, 0), (85, 28, 93), (173, 36, 97), 
    (246, 219, 44), (44, 172, 112), (215, 130, 165), (215, 56, 27), (235, 164, 191), (156, 24, 23)
    ]

def row_maker(y):
    for x in range(-250,250,50):
        bob.penup()
        bob.setpos(x,y*50-250)
        bob.pendown()
        bob.dot(20,random.choice(colors))

for i in range(10):
    row_maker(i)

screen = Screen()
screen.exitonclick()