from turtle import Turtle
class Snake:
    def __init__(self):
        self.segment = []
        self.positions = [(0, 0), (-10, 0), (-20, 0), (-30, 0)]
        self.create()
    def create(self):
        positions = self.positions
        for i in positions:
            segment = Turtle()
            segment.penup()
            segment.shape("square")
            segment.goto(i)
            segment.color('white')
            self.segment.append(segment)
    def move(self):
        global segments
        segments = self.segment
        for i in range(len(segments)-1, 0, -1):
            x = segments[i - 1].xcor()
            y = segments[i-1].ycor()
            segments[i].goto(x, y)
        segments[0].forward(10)
    def left(self):
        n = self.segment[0].heading()
        if n != 0:
            self.segment[0].setheading(180)
    def right(self):
        n = self.segment[0].heading()
        if n != 180:
            self.segment[0].setheading(0)
    def up(self):
        n = self.segment[0].heading()
        if n != 270:
            self.segment[0].setheading(90)
    def down(self):
        n = self.segment[0].heading()
        if n != 90:
            self.segment[0].setheading(270)
    def reset(self):
        for i in self.segment:
            i.color('black')
        self.segment = []
        self.create()
    def new_segment1(self):
        # snake = Snake()
        segment = Turtle()
        segment.shape("square")
        segment.penup()
        segment.speed("fastest")
        segment.hideturtle()
        position = self.segment[-1].position()
        segment.goto(position)
        self.segment.append(segment)
        self.segment[len(self.segment) - 1].showturtle()
        self.segment[len(self.segment) - 1].color("white")
