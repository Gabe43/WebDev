from turtle import Turtle,Screen
score = Turtle()
over = Turtle()
class Score:
    
    def __init__(self):
        self.score = 0
        score.hideturtle()
        score.color('white')
        score.penup()
        score.goto(x=-150,y=270)
        self.update()
    
    def update(self):
        score.write(align='center', arg =f"Score : {self.score}",font=("Arial", 16 , "normal"))
    
    def game_over(self):
        over.hideturtle()
        over.color('white')
        over.penup()
        over.write(align='center', arg ="GAME OVER",font=("Arial", 22 , "normal"))
    
    def increment(self):
        self.score = self.score+1
        z = self.score
        with open('score.txt') as fl:
            ab = fl.read()
            ac = int(ab)
            if z>ac:
                with open('score.txt','w') as file:
                    sc = file.write(f'{z}')
        score.clear()
        self.update()

    