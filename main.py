import time
from turtle import Screen
from my_modules.snake import Snake
from my_modules.food import Food
from my_modules.scoreboard import Scoreboard

# set up the screen to display the game using the turtle screen.
screen = Screen()
screen.setup(width=580, height=500)
screen.bgcolor("black")
screen.title("Mitchell's snake game")
screen.tracer(0)

# create instances of the snake, food and scoreboard.
snake = Snake()
food = Food()
score = Scoreboard()

# make the screen listen to our input
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    # detect collision with food
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        score.increase()

    # detect collision with wall
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -290
        or snake.head.ycor() > 240
        or snake.head.ycor() < -245
    ):
        score.reset()
        snake.reset()

        # score.game_over()

    # detect collision with body
    for block in snake.snake_objects[1:]:
        if snake.head.distance(block) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()
