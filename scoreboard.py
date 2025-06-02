from turtle import Turtle


def read_score():
    with open('score_file.txt') as score_data:
        current_score = int(score_data.read().strip())
        return current_score


def write_score(score):
    with open('score_file.txt', 'w') as score_data:
        score_data.write(str(score))


class Scoreboard(Turtle):
    ALIGNMENT = "center"
    FONT = ('Arial', 15, 'normal')

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.high_score = read_score()
        self.color("white")
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",
                   align=self.ALIGNMENT, font=self.FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            write_score(self.high_score)
        self.score = 0
        self.update_score()