from pickle import GET
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import InputRequired, URL
import csv


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[InputRequired()])
    location = StringField(
        'Cafe Location on Google Maps(URL)', validators=[InputRequired(), URL()])
    opening_time = StringField(
        'Opening Time e.g.8AM', validators=[InputRequired()])
    closing_time = StringField(
        'Closing Time e.g.5:30PM', validators=[InputRequired()])
    coffee_rating = SelectField('Coffee Rating', choices=[
                                '✘', '☕️', '☕️☕️', '☕️☕️☕️', '☕️☕️☕️☕️', '☕️☕️☕️☕️☕️'])
    wifi_rating = SelectField('Wifi Strength Rating', choices=[
                              '✘', '💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪'])
    power_socket = SelectField('Power Socket Available', choices=[
                               '✘', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
#     Another Way of Checking the url
#     import validators
#     valid=validators.url('https://www.codespeedy.com/')
#     if valid==True:
#         print("Url is valid")
#     else:
#         print("Invalid url")
    if form.validate_on_submit():
        data = [values for keys, values in form.data.items()]
        data.pop(len(data)-1)
        data.pop(len(data)-1)
        print("True")
        with open('cafe-data.csv', 'a', newline='', encoding="utf-8") as f:
            write = csv.writer(f)
            write.writerow(data)

    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        len_rows = len(list_of_rows)
        len_colomns = len(list_of_rows[1])
    return render_template('cafes.html', cafes=list_of_rows, rows=len_rows, colmn=len_colomns)


if __name__ == '__main__':
    app.run(debug=True)
