from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Email, InputRequired, Length
from flask_bootstrap import Bootstrap

class MyForm(FlaskForm):
    name = StringField(label='Email', validators=[InputRequired(), Email()])
    password = PasswordField(label='Password', validators=[
                             InputRequired(), Length(min=8)])
    submit = SubmitField(label='Log In')


app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = MyForm(meta={'csrf': False})
    if form.validate_on_submit():
        if form.name.data == 'admin@email.com' and form.password.data == '12345678':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
