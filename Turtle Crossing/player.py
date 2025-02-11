from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.reset_player()

    def move_up(self):
        self.setheading(90)
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.setheading(270)
        self.forward(MOVE_DISTANCE)

    def move_left(self):
        self.setheading(180)
        self.forward(MOVE_DISTANCE)

    def move_right(self):
        self.setheading(0)
        self.forward(MOVE_DISTANCE)

    def reset_player(self):
        self.goto(STARTING_POSITION)
        self.setheading(90)
