from turtle import Turtle
start_pos = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
class Snake():
    def __init__(self):
        self.segments = []
        self.create()
        self.head = self.segments[0]

    def create(self):
        for position in start_pos:
            self.add_segment(position)

    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        self.segments.append(new_segment)
        new_segment.goto(position)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, - 1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        head = self.head
        if head.heading() != 270:
            head.setheading(90)

    
    def down(self):
        head = self.segments[0]
        if head.heading() != 90:
            head.setheading(270)

    def left(self):
        head = self.segments[0]
        if head.heading() != 0:
            head.setheading(180)
            

    def right(self):
        head = self.segments[0]
        if head.heading() != 180:
            head.setheading(0)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create()
        self.head = self.segments[0]