from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """Models the qualities of a snake"""

    def __init__(self):
        self.snake_objects = []
        self.create_snake()
        self.head = self.snake_objects[0]

    def create_snake(self):
        """creates a snake depending on the amount used in the form of a list"""
        for position in POSITIONS:
            self.add_block(position)

    def add_block(self, position):
        """Adds to the length of the snake"""
        block = Turtle("square")
        block.color("white")
        block.penup()
        block.goto(position)
        self.snake_objects.append(block)

    def extend(self):
        self.add_block(self.snake_objects[-1].position())

    def reset(self):
        """Puts the snake at the center of the screen if it collides with a wall"""
        for snake in self.snake_objects:
            snake.goto(1000, 1000)
        self.snake_objects.clear()
        self.create_snake()
        self.head = self.snake_objects[0]

    def move_snake(self):
        """Moves the snake"""
        for number in range(len(self.snake_objects) - 1, 0, -1):
            new_x = self.snake_objects[number - 1].xcor()
            new_y = self.snake_objects[number - 1].ycor()
            self.snake_objects[number].goto(new_x, new_y)
        self.snake_objects[0].forward(20)

    def up(self):
        """moves the snake up except if it's facing downwards"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """moves the snake down except if it's facing upwards """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        """moves the snake right except if it's facing left"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        """moves the snake left except if it's facing right"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
