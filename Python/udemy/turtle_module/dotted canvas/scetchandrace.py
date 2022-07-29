# from turtle import Turtle, Screen
# bob = Turtle()
# screen = Screen()
# screen.listen()
# def move_forward():
#     bob.forward(10)
# screen.onkey(key='w', fun = move_forward)
# def move_back():
#     bob.back(10)
# screen.onkey(key='s', fun = move_back)
# def move_right():
#     bob.right(10)
# screen.onkey(key='d', fun = move_right)
# def move_left():
#     bob.left(10)
# screen.onkey(key='a', fun = move_left)
# def clear():
#     bob.clear()
# screen.onkey(key='c', fun = clear)
# screen.exitonclick()

from turtle import Turtle, Screen, window_width
import random
import turtle
screen = Screen()
bob = Turtle()
bob.color('red')
bob.shape('turtle')
tom = Turtle()
tom.color('orange')
tom.shape('turtle')
bom = Turtle()
bom.color('yellow')
bom.shape('turtle')
dom = Turtle()
dom.color('green')
dom.shape('turtle')
com = Turtle()
com.color('blue')
com.shape('turtle')
pom = Turtle()
pom.color('violet')
pom.shape('turtle')
guess = screen.textinput(title="Whtat's your Bet", prompt="Which color do you like to choose")
bob.penup()
bob.goto(-window_width()/2.07,-100)
tom.penup()
tom.goto(-window_width()/2.07,-60)
bom.penup()
bom.goto(-window_width()/2.07,-20)
dom.penup()
dom.goto(-window_width()/2.07,20)
com.penup()
com.goto(-window_width()/2.07,60)
pom.penup()
pom.goto(-window_width()/2.07,100)
i = 330
while (i<457):
    bob.speed(random.randint(1,10))
    bob.forward(random.randint(1,10))
    tom.speed(random.randint(1,10))
    tom.forward(random.randint(1,10))
    bom.speed(random.randint(1,10))
    bom.forward(random.randint(1,10))
    dom.speed(random.randint(1,10))
    dom.forward(random.randint(1,10))
    com.speed(random.randint(1,10))
    com.forward(random.randint(1,10))
    pom.speed(random.randint(1,10))
    pom.forward(random.randint(1,10))
    if (bob.position()>(315.00,-100.00)):
        ab = 'red'
        break
    elif (tom.position()>(315.00,-60.00)):
        ab = 'orange'
        break
    elif (bom.position()>(315.00,-20.00)):
        ab = 'yellow'
        break
    elif (dom.position()>(315.00,20.00)):
        ab = 'green'
        break
    elif (com.position()>(315.00,60.00)):
        ab = 'blue'
        break
    elif (pom.position()>(315.00,100.00)):
        ab = 'violet'
        break
screen.bye()
if guess==ab:
    print(f"You Won. The winner is {ab} turtle")
else:
    print(f"You Lose. The winner is the {ab} turtle")




