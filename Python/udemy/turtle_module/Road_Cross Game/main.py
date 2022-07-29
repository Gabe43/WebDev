from turtle import Turtle, Screen
from cars import Cars
from character import Character
import time

from score import Score
screen = Screen()
screen.setup(width=800,height=600)
screen.listen()
screen.tracer(0)


turtle = Character()
cars = Cars()
score = Score()
i = 0
screen.onkey(key='Up', fun=turtle.movement)
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move()
    for car in cars.cars_list:
        if turtle.distance(car)<20:
            game_is_on=False
    if turtle.ycor()>=290:
        score.increment()
        turtle.goto(0,-280)
        turtle.incre()
        cars.speed_increment()   
screen.exitonclick()
