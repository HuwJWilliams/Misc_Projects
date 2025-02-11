from turtle import Turtle

MOVE_DISTANCE = 20


class Snake:
    def __init__(
        self,
        colour: str = "white",
        shape: str = "square",
        move_distance: int = MOVE_DISTANCE,
    ):

        self.segment_ls = []
        self.shape = shape
        self.colour = colour
        self.move_distance = move_distance
        self.snake_heading = 0

        self.make_init_snake()

        self.head = self.segment_ls[0]

    def make_body_piece(self, xy_coordinate: tuple = (0, 0)):
        t = Turtle()
        t.penup()
        t.color(self.colour)
        t.shape(self.shape)
        t.setpos(xy_coordinate)
        t.setheading(self.snake_heading)

        return t

    def make_init_snake(
        self,
    ):
        for i in range(3):
            xy_coordinate = (-20 * i, 0)
            t = self.make_body_piece(xy_coordinate)
            self.segment_ls.append(t)
        return self.segment_ls

    def move_forwards(self):

        for seg_num in range(len(self.segment_ls) - 1, 0, -1):
            new_x = self.segment_ls[seg_num - 1].xcor()
            new_y = self.segment_ls[seg_num - 1].ycor()
            self.segment_ls[seg_num].goto(new_x, new_y)
        self.head.forward(self.move_distance)

        return self.segment_ls

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
            self.snake_heading = 90

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
            self.snake_heading = 270

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
            self.snake_heading = 0

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
            self.snake_heading = 180

    def extend(self):
        xy_coordinate = self.segment_ls[-1].position()
        t = self.make_body_piece(xy_coordinate)
        self.segment_ls.append(t)

    def reset(self):
        for seg in self.segment_ls:
            seg.goto(1000, 1000)
        self.segment_ls.clear()
        self.make_init_snake()
        self.head = self.segment_ls[0]
