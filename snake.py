from turtle import Turtle


class Snake(Turtle):
    STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
    UP = 90
    LEFT = 180
    DOWN = 270
    RIGHT = 0

    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in self.STARTING_POSITIONS:
            self.add_segments(pos)

    def add_segments(self, pos):
        new_seg = Turtle()
        new_seg.shape("square")
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(pos)
        self.segments.append(new_seg)

    def extend_snake(self):
        self.add_segments(self.segments[-1].pos())

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            x_cor = self.segments[seg - 1].xcor()
            y_cor = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x_cor, y_cor)

        self.segments[0].forward(20)

    def move_up(self):
        if self.head.heading() != self.DOWN:
            self.head.setheading(self.UP)

    def move_down(self):
        if self.head.heading() != self.UP:
            self.head.setheading(self.DOWN)

    def move_left(self):
        if self.head.heading() != self.RIGHT:
            self.head.setheading(self.LEFT)

    def move_right(self):
        if self.head.heading() != self.LEFT:
            self.segments[0].setheading(self.RIGHT)

    def check_border(self):
        if self.head.xcor() > 280 or self.head.xcor() < -280 or self.head.ycor() > 280 or self.head.ycor() < -280:
            return True
