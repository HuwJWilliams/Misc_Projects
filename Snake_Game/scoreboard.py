from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0

        try:
            with open("high_score.txt", "r") as file:
                self.high_score = int(file.read())

        except FileNotFoundError:
            with open("high_score.txt", "w") as file:
                file.write("0")
                self.high_score = 0

        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score}  |  High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

            with open("high_score.txt", "w") as file:
                file.write(str(self.high_score))

        self.score = 0
        self.update_scoreboard()
