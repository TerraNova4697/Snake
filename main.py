from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collisions with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.add_score()

    # Detect collisions with walls
    if snake.head.xcor() >= 295 or snake.head.ycor() >= 295 or snake.head.xcor() <= -310 or snake.head.ycor() <= -300:
        scoreboard.reset()
        snake.reset()

    # Detect collisions with the tail
    for block in snake.blocks[1:]:
        if snake.head.distance(block) < 10:
            scoreboard.reset()
            snake.reset()





screen.exitonclick()
