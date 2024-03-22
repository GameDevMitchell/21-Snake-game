from turtle import Turtle
from random import randint


class Food(Turtle):
    """A simple attempt to model the food of a snake game"""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Creates a new random x and y and gets the food to go there"""
        random_x = randint(-270, 270)
        random_y = randint(-230, 230)
        self.goto(random_x, random_y)
