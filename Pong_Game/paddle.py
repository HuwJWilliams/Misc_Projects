from turtle import Turtle

MOVE_SPEED = 20
PADDLE_SIZE = (5, 1)


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()

        self.position = position
        self.shape("square")
        self.shapesize(stretch_wid=PADDLE_SIZE[0], stretch_len=PADDLE_SIZE[1])
        self.penup()
        self.speed("fastest")
        self.goto(self.position)
        self.color("white")

    def go_up(self):
        if self.position[1] >= 240:
            pass

        else:
            new_position = (self.position[0], self.position[1] + MOVE_SPEED)
            self.goto(new_position)
            self.position = new_position

    def go_down(self):
        if self.position[1] <= -240:
            pass

        else:
            new_position = (self.position[0], self.position[1] - MOVE_SPEED)
            self.goto(new_position)
            self.position = new_position
