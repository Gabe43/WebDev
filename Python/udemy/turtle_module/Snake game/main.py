from turtle import Screen, width, window_width
from food import Food
import random
from high_score import High_Score
from score import Score
from snake import Snake
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)




snake = Snake()
food = Food()
score = Score()
high_sco = High_Score()
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True
while(game_is_on):
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food.position())< 15:
        food.goto(random.randint(-280,280), random.randint(-280,280))
        snake.extend()
        score.increment()
    if snake.xcor()>280 or snake.xcor()<=-300 or snake.ycor()>290 or snake.ycor()<=-290:
        score.game_over()
        break

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 5:
            score.game_over()
            game_is_on=False
            break    
    

screen.exitonclick()