from turtle import Turtle, xcor


class Ball(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.create_circle()
        self.z = self.position()
        self.x_move = 10
        self.y_move = 10
        

    def create_circle(self):
        self.color('white')
        self.shape('circle')
        self.penup()
        
    
    def movement(self):
            new_x = self.xcor() + self.x_move
            new_y = self.ycor() + self.y_move 
            self.goto(new_x,new_y)           
           

    def bounce_y(self):
        self.y_move = self.y_move*-1
                


    def bounce_x(self):
            self.x_move = self.x_move*-1

    
    def reset_position(self):
        self.goto(self.z)
        self.bounce_x()