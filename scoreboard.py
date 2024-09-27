from turtle import Turtle


class Scoreboard(Turtle):
    FONT = ('Arial', 14, 'normal')
    ALIGN = "center"

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.score = 0
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align=self.ALIGN, font=self.FONT)

    def game_over(self):
        self.goto(0, 0)
        self.score = 0
        self.write("GAME OVER !!!", align=self.ALIGN, font=self.FONT)
