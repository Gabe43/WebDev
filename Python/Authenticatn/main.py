from flask import Flask, render_template, request, url_for, redirect, send_from_directory, flash
import flask
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
# db.create_all()


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        nam = request.form.get('name')
        eml = request.form.get('email')
        passwrd = generate_password_hash(password=request.form.get('password'),method='pbkdf2:sha256',salt_length=8)
        new_user = User(email=eml,password=passwrd,name=nam)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(f'/secrets/{nam}')
    return render_template("register.html")



@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        eml = request.form.get('email')
        passwrd = request.form.get('password')
        user =  User.query.filter_by(email=eml).first()
        if check_password_hash(pwhash=user.password,password=passwrd):
            login_user(user)
            flask.flash('Logged in successfully.')
            return redirect(f'/secrets/{user.name}')
        else:
            flask.flash('Password incorrect, Please try again!')
    return render_template("login.html")


@app.route('/secrets/<name>')
@login_required
def secrets(name):
    return render_template("secrets.html",nm=name)
        


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory(directory='static/files', path='cheat_sheet.pdf', as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
