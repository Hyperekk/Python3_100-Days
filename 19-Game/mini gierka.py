from turtle import Turtle, Screen

bob = Turtle()
screen = Screen()

def move_forwards():
    bob.forward(20)

def move_backwards():
    bob.backward(20)

def left():
    pos = bob.heading()
    bob.setheading(pos + 10)

def right():
    pos = bob.heading()
    bob.setheading(pos - 10)


screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="a", fun=left)
screen.onkeypress(key="d", fun=right)
screen.onkey(key="c",fun=screen.resetscreen)


screen.exitonclick()