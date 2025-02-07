from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def write_scoreboard(self, pos, score):
        self.goto(pos)
        self.write(
            f"{score}",
            align="center",
            font=("Courier", 30, "bold"),
        )

    def update_scoreboard(self):
        self.clear()
        self.left_scoreboard = self.write_scoreboard(
            pos=(-100, 240), score=self.l_score
        )
        self.right_scoreboard = self.write_scoreboard(
            pos=(100, 240), score=self.r_score
        )
