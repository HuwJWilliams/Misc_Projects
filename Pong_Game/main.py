from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Screen Setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# Paddle Setup
l_paddle = Paddle((-380, 0))
r_paddle = Paddle((380, 0))

# Ball Setup

ball = Ball()

# Scoreboard Setup
scoreboard = Scoreboard()

# Controls
screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "i")
screen.onkey(r_paddle.go_down, "k")

# Game Loop
game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if (
        ball.xcor() > 360
        and r_paddle.distance(ball) < 50
        or ball.xcor() < -360
        and l_paddle.distance(ball) < 50
    ):
        ball.bounce_x()
        ball.increase_speed()

    elif ball.xcor() > 380:
        scoreboard.l_score += 1
        scoreboard.update_scoreboard()
        ball.reset_position()

    elif ball.xcor() < -380:
        scoreboard.r_score += 1
        scoreboard.update_scoreboard()
        ball.reset_position()


# Exit Screen
screen.exitonclick()
