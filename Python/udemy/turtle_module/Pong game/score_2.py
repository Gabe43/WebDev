from turtle import Turtle

score = Turtle()

class Score_2(Turtle):
    def __init__(self,i,j) -> None:
        super().__init__()
        self.create_score(i,j)


    def create_score(self,i,j):
        self.score = 0
        score.color('white')
        score.penup()
        score.goto(x=i,y=j)
        score.hideturtle()
        self.update()
        

    def update(self):
        score.write(arg=f'{self.score}',font=('Arial', 25, 'normal'))

    def increment(self):
        self.score = self.score+1
        score.clear()
        self.update()

        

        
        