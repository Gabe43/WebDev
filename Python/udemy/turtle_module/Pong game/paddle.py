from turtle import Turtle

class Bar(Turtle):
    
    def __init__(self,a,b) -> None:
        super().__init__()
        self.create_paddle(a,b)

    def create_paddle(self,a,b):
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.penup()
        self.goto(x=a,y=b)

    def up(self):
        new_y = self.ycor()+20
        self.goto(self.xcor(),new_y)
    
    def down(self):
        new_y = self.ycor()-20
        self.goto(self.xcor(),new_y)
    
    
   