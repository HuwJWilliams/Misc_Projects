# %%
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake(colour="white", shape="square")
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")
screen.onkey(snake.left, "a")

screen.update()

game_is_on = True
while game_is_on == True:
    screen.update()
    time.sleep(0.1)

    snake.move_forwards()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update_score()

    # Detect collision with wall
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 260
        or snake.head.ycor() < -280
    ):
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    # if head collides with any segment in the tail:
    for segment in snake.segment_ls[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

# Screen Exit
screen.exitonclick()
