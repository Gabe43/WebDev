from turtle import Turtle, Screen
import turtle
import pandas

from segements import Segments
screen = Screen()
segments = Segments()
screen.setup(width=730, height=510)
screen.bgpic('blank_states_img.gif')
data = pandas.read_csv('50_states.csv')
list_x = data['x'].to_list()
list_y = data['y'].to_list()
position = [(list_x[i],list_y[i]) for i in range(0,len(list_x))]
states = data['state'].to_list()
game_is_on = True
z = len(states)
i = 0
while(game_is_on):
    name = screen.textinput(f"{i}/{z} States Correct", "What's another state name")
    for item in states:
        if name.title() == item:
            segments.create_segments(item,position[states.index(item)])
            i = i+1
    if (name == 'exit'):
        game_is_on = False
    
    




screen.exitonclick()
