from turtle import Turtle 

class High_Score():
    def __init__(self) -> None:
        super().__init__()
        self.high_score()

    def high_score(self):
        with open('score.txt') as file:
            score = file.read()
            score_int = int(score)
        turtle = Turtle()
        turtle.color('white')
        turtle.hideturtle()
        turtle.penup()        
        turtle.goto(x=50,y=270)
        turtle.write(arg=f'High Score : {score_int}', font=('Ariel', 16))
        