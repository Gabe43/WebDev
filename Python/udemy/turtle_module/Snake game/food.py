from turtle import Turtle
import random

food = Turtle()

class Food():
    
    def __init__(self):
        super().__init__()
        food.shape('circle')
        food.color('blue')
        food.shapesize(stretch_wid=0.4, stretch_len=0.4)
        food.penup()
        food.speed('fastest')
        food.goto(random.randint(-280,280), random.randint(-280,280))
    
      
    
    def position(self):
        return food.position()
    
    def goto(self,x,y):
        food.goto(x,y)