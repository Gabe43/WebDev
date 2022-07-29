from flask import Flask

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return '<h1 style="text-align:center">Hello, World!</h1><p>This is a text</p><img src="https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif"></img>'

# @app.route('/username/<name><int:number>')
# def greet(name,number):
#     return f'Hello {name}, you are {number} years old'


def bold(func):
    def turn():
        text = func()
        return f'<b>{text}</b>'
    return turn

def italic(func):
    def turn():
        text = func()
        return f'<em>{text}</em>'
    return turn
def underline(func):
    def turn():
        text = func()
        return f'<u>{text}</u>'
    return turn


@app.route('/')
@bold
@underline
def bye():
    return "Bye!"

if __name__== '__main__':
    app.run(debug=True)








