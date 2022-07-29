from turtle import Turtle, Screen, exitonclick, window_width
import random
bob = Turtle()
bop = Turtle()
screen = Screen()
bob.color('red')
bob.shape('turtle')
bop.color('green')
bop.shape('turtle')
bob.penup()
bop.penup()
bop.goto(-window_width()/2.07,-60)
bob.goto(-window_width()/2.07,-100) #330
z = bob.distance(window_width()/5,0) #477
i = 330
while (i<478):
    bob.speed(random.randint(1,10))
    bob.forward(random.randint(1,10))
    bop.speed(random.randint(1,10))
    bop.forward(random.randint(1,10))
    print(bob.position())
    if (bob.position()>(312.00,-100.00)):
        print(f"The Winner is Red Turtle")
        break
    elif (bop.position()>(312.00,-60)):
        print(f"The Winner is Green Turtle")
        break
    i = i+1
screen.bye()

    

