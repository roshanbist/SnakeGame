from turtle import Screen, Turtle
import time

from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
new_score = Scoreboard()

screen.listen()

screen.onkey(snake.move_up, 'Up')
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")
game_on = True


while game_on:
    screen.update()
    time.sleep(0.12)
    snake.move()

    if snake.head.distance(food) < 15:
        food.shift_food_location()
        new_score.score += 1
        new_score.update_score()
        snake.extend_snake()

    if snake.check_border():
        new_score.reset()
        snake.reset()

    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 15:
            new_score.reset()
            snake.reset()

screen.exitonclick()
