from turtle import Turtle,Screen
import random
SCREEN = Screen()

Z = 0
class Cars():
    def __init__(self) -> None:
        self.speed = 5
        self.speed_incre = 5
        self.cars_list = []
    

    def create_car(self):
        SCREEN.colormode(255)
        car = Turtle()      
        car.fillcolor(random.randint(0,255), random.randint(100,255), random.randint(110,255))
        car.shape('square')
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.left(180)
        y = random.randint(-240,240)
        x = random.randint(420,450)
        car.penup()
        car.goto(x,y)
        self.cars_list.append(car)

    def move(self):
        for car in self.cars_list:
            car.forward(self.speed)
    
    def speed_increment(self):
       self.speed = self.speed+self.speed_incre
    
    