import os
from turtle import Turtle, Screen
from create_the_snake import Snake
from scoreboard import Scoreboard
from food import Food
sc = Screen()
sc.setup(600, 600)
sc.bgcolor("black")
snake = Snake()
score = Scoreboard()
food = Food()
game = 1
score.update()
sc.listen()
sc.onkey(snake.left, "Left")
sc.onkey(snake.right, "Right")
sc.onkey(snake.up, "Up")
sc.onkey(snake.down, "Down")
while game:
    sc.update()
    snake.move()
    if snake.segment[0].distance(food) < 15:
        food.refresh()
        score.update1()
        snake.new_segment1()
    elif snake.segment[0].xcor() < -280 or snake.segment[0].xcor() > 280 or snake.segment[0].ycor() > 280 or snake.segment[0].ycor() < -280:
        score.reset()
        snake.reset()
        score.update_score1()
sc.exitonclick()
