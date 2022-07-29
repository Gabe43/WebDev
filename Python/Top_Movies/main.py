from traceback import print_tb
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from numpy import sort
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-movies-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(250), unique=True, nullable=False)
    img_url = db.Column(db.String(250), unique=True, nullable=False)


# db.create_all()

# # new_movie = Movie(
# #     title="Phone Booth",
# #     year=2002,
# #     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
# #     rating=7.3,
# #     ranking=10,
# #     review="My favourite character was the caller.",
# #     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# # )
# # db.session.add(new_movie)
# # db.session.commit()

movie_database_api = 'd2d7ce015f741a6d3d29c715b63fd08e'
movie_database_url = 'https://api.themoviedb.org/3/search/movie'


movies = []
movie_id = []


@app.route("/")
def home():
    mv = []
    movie = Movie.query.all()
    leng = len(movie)
    if leng>1:
        for item in movie:
            mv.append(item.rating)
        for itm in range(0,len(mv)):
            data = Movie.query.filter_by(rating=mv[itm]).all()[0]
            data.ranking = itm+1
            db.session.commit()
    return render_template("index.html", movies=movie, length=leng)


@app.route("/edit/<int:num>", methods=['GET', 'POST'])
def edit(num):
    movie = Movie.query.all()[num]
    mv = []
    x = None
    if request.method == 'POST':
        new_rating = request.form.get('new_rating')
        new_review = request.form.get('new_review')
        if len(new_rating) > 0:
            movie.rating = new_rating
        elif len(new_review) > 0:
            movie.review = new_review
        db.session.commit()
        movi = Movie.query.all()
        leng = len(movi)
        for item in range(0, leng):
            for itm in range(item+1, leng):
                if movi[item].rating < movi[itm].rating:
                    mv = [movi[item].title,movi[item].year,movi[item].rating,movi[item].review,movi[item].description,movi[item].img_url,movi[item].ranking]
                    db.session.delete(movi[item])
                    db.session.commit()
                    new_movie = Movie(title=mv[0], year=mv[1], description=mv[4], rating=mv[2], review=mv[3], img_url=mv[5], ranking=mv[6])
                    db.session.add(new_movie)
                    db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html')


@app.route("/delete/<int:num>", methods=['GET', 'POST'])
def delete(num):
    movie = Movie.query.all()[num]
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        new_movie = request.form.get('fmovie')
        parms = {
            'api_key': movie_database_api,
            'query': new_movie
        }
        data = requests.get(url=movie_database_url, params=parms)
        movie = data.json()
        movie_list = movie.get('results')
        for item in range(0, len(movie_list)):
            movies.append(
                f"{movie_list[item].get('title')} - {movie_list[item].get('release_date')}")
            movie_id.append(f"{movie_list[item].get('id')}")
        movie_list.clear()
        return redirect(url_for('select'))
    return render_template('add.html')


@app.route("/select")
def select():
    return render_template('select.html', mov=movies, length=len(movies))


@app.route("/select/<int:numb>")
def selection(numb):
    movies.clear()
    id = movie_id[numb]
    movie_id.clear()
    movie_details = f'https://api.themoviedb.org/3/movie/{id}'
    parms = {
        'api_key': movie_database_api
    }
    data = requests.get(url=movie_details, params=parms)
    movie = data.json()
    path = movie.get('poster_path')
    movie_img = f'https://image.tmdb.org/t/p/w500{path}'
    new_movie = Movie(title=movie.get('original_title'), year=movie.get('release_date'), description=movie.get(
        'overview'), rating=movie.get('vote_average'), review=movie.get('tagline'), img_url=movie_img, ranking=Movie.query.count()+1)
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('edit', num=Movie.query.count()-1))


if __name__ == '__main__':
    app.run(debug=True)

