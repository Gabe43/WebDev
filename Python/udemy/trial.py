from turtle import Screen, Turtle, width 
import random
import time
screen = Screen()
screen.setup(height=600,width=600)
screen.listen()
screen.colormode(255)

car = Turtle()
car.shape('square')
car.shapesize(stretch_len=4,stretch_wid=1)
car.penup()
car.goto(x=-260,y=0)

food = Turtle()
food.shape('circle')
food.shapesize(stretch_len=0.5,stretch_wid=0.5)

def movement():
    car.forward(10)
    print(car.distance(food))
    if car.distance(food)==40.0:
        for item in range(1,100):
            time.sleep(0.1)
            car.color(random.randint(100,255),random.randint(100,255),random.randint(100,255))


screen.onkey(key='w',fun=movement)

    






screen.mainloop()