from turtle import Turtle

POSITIONS = []
for item in range(290,-300, -30):
    POSITIONS.append(item)

class Line(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.create_line()

        
    def create_line(self):  
        for position in POSITIONS:
            segment = Turtle()
            segment.color('white')
            segment.shape('square')
            segment.shapesize(stretch_len=0.2, stretch_wid=1)
            segment.penup()
            segment.goto(0,position)