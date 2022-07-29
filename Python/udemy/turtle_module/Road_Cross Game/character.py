from turtle import Turtle

class Character(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.forw  = 10
        self.incry = 5 
        self.create_turtle()

    
    def create_turtle(self):
        self.color('black')
        self.shape('turtle')
        self.left(90)
        self.penup()
        self.goto(0,-280)

    def movement(self):
        self.forward(self.forw)

    def incre(self):
        self.forw = self.forw+self.incry
