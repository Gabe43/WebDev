from turtle import Turtle
score = Turtle()

class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.create_score()
    
    def create_score(self):
        self.score= 1
        self.color('black')
        self.penup()
        self.goto(x=-380,y=250)
        self.hideturtle()
        self.update_score()
        
    def update_score(self):
        self.write(arg=f'Level {self.score}', font=('Ariel',20))
    
    def increment(self):
        self.score = self.score+1
        self.clear()
        self.update_score()
        
        