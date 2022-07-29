from flask import request
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/details",methods=['POST'])
def details():
    nm = request.form['fname']
    ps = request.form['passwrd']
    return render_template('details.html',n=nm,p=ps)

if __name__=='__main__':
    app.run(debug=True)


