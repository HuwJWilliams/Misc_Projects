from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.x_speed = 3
        self.y_speed = 3
        self.move_speed = 0.0001
        self.position = (0, 0)

    def move(self):
        new_x = self.xcor() + self.x_speed
        new_y = self.ycor() + self.y_speed
        self.goto(new_x, new_y)
        self.position = (new_x, new_y)

    def bounce_y(self):
        self.y_speed *= -1

    def bounce_x(self):
        self.x_speed *= -1
        self.move_speed *= 0.0001

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0
        self.bounce_x()
