from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')
@app.route('/guess/<name>')
def guess(name):
    parms = {
        'name': f'{name}'
    }
    # Agify
    response = requests.get('https://api.agify.io', params=parms)
    age = response.json()['age']

    # Genderize
    response = requests.get('https://api.genderize.io?', params=parms)
    gender = response.json()['gender']
    
    return render_template('index.html',ag = age, gen = gender,nm = name)


@app.route('/vlog/<num>')
def blog(num):
    print(num)
    vlog_url = ' https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(vlog_url)
    all_posts = response.json()
    return render_template('vlog.html',posts=all_posts)

if __name__ == '__main__':
    app.run(debug=True)
