import colorgram as cg
from turtle import Turtle, Screen
import random
screen = Screen()
color_list = cg.extract("img.jpeg", 2 ** 32)
color_palette = []

for count in range(len(color_list)):
    rgb = color_list[count]
    color = rgb.rgb
    color_palette.append(color)
bob = Turtle()
screen.colormode(255)
bob.speed('fastest')
ab = 0
while (ab<5):
    i = 0
    while (i<9):
        x = random.choice(color_palette)
        bob.pencolor(x)
        bob.dot(10)
        bob.penup()
        bob.forward(20)
        i = i+1
    bob.dot(10, random.choice(color_palette))
    bob.left(90)
    bob.forward(20)
    bob.left(90)
    bob.penup()
    m = 0
    while(m<9):
        y = random.choice(color_palette)
        bob.pencolor(y)
        bob.dot(10)
        bob.penup()
        bob.forward(20)
        m = m+1
    bob.dot(10, random.choice(color_palette))
    bob.right(90)
    bob.forward(20)
    bob.right(90)
    bob.penup()
    n = 0
    while(m<9):
        h = random.choice(color_palette)
        bob.pencolor(h)
        bob.dot(10)
        bob.penup()
        bob.forward(20)
        n = n+1
    ab = ab+1



screen.exitonclick()


