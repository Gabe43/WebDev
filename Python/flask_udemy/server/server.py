
from random import random
from flask import Flask
import random

app = Flask(__name__)

a = random.randint(0,9)

@app.route('/')
def find():
    return '<h1>Guess a number between 0 and 9</h1><img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"></img>'


@app.route("/<int:number>")
def num(number):
    lst = ['red','green','blue','yellow','violet','pink','orange']
    clr = random.choice(lst)
    if number>a:
        return f'<h1 style="color:{clr};">To High,try again!</h1><img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"></img>'
    elif number<a:
        return '<h1 style="color:{clr};">To Low,try again!</h1><img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"></img>'
    elif number==a:
        return '<h1>You found me!</h1><img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"></img>'
    


if __name__== '__main__':
    app.run(debug=True)