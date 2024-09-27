from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("white")
        self.shift_food_location()

    def shift_food_location(self):
        x_pos = random.randrange(-260, 260, 20)
        y_pos = random.randrange(-260, 260, 20)
        self.speed('fastest')
        self.goto(x_pos, y_pos)
