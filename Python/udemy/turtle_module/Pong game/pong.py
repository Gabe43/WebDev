from turtle import Turtle, Screen, down, position, tracer, width
from ball import Ball
import time
from line import Line
from paddle import Bar
from score_1 import Score_1
from score_2 import Score_2


screen = Screen()
screen.listen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.tracer(0)


bar = Bar(-350,0)
bar_2 = Bar(350,0)
ball = Ball() 
line = Line()
score = Score_1(-80,260)
score_1 = Score_2(80,260)

screen.onkey(key='Up', fun=bar_2.up)
screen.onkey(key='Down', fun=bar_2.down)
screen.onkey(key='w', fun=bar.up)
screen.onkey(key='s', fun=bar.down)


z = 0.10 
x = 0
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(z)
    ball.movement()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    elif ball.distance(bar_2)<40 and ball.xcor()<=340 or ball.distance(bar)<40 and ball.xcor()>=-340:
        ball.bounce_x()
        if (z>0.01):
            z = z-0.005
            x = z
    elif ball.xcor()==380:
        score.increment()
        ball.reset_position()
        
    elif ball.xcor()==-380:
        score_1.increment()
        ball.reset_position()
    
    print(z)

    
    
    



screen.exitonclick()

