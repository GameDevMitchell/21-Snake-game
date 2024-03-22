from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    """Represents the score board in the turtle game"""

    def __init__(self):
        super().__init__()
        self.score = 0
        try:
            with open("my_modules\data.txt") as file:
                score = int(file.read())
                self.high_score = score
        except ValueError:
            self.high_score = 0
        except FileNotFoundError:
            with open("my_modules\data.txt", mode="w") as file:
                file.write(f"{0}")
        self.high_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-1, 210)
        self.update()

    def increase(self):
        self.score += 1
        self.update()

    def update(self):
        self.clear()
        self.write(
            f"score: {self.score} High Score: {self.high_score}", False, ALIGNMENT, FONT
        )

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("my_modules\data.txt", mode="w") as file:
                file.write(f"{self.score}")
        self.score = 0
        self.update()
