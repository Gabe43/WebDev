from turtle import Turtle

class Segments(Turtle):
    def __init__(self) -> None:
        super().__init__()

    def create_segments(self,name,position):
        states = Turtle()
        states.penup()
        states.goto(position)
        states.speed('slow')        
        states.hideturtle()
        states.write(name)

