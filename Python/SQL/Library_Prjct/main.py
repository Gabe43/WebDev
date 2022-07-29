from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'


db.create_all()

all_books = []

@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template('index.html', books=all_books, length=len(all_books))


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        book_name = request.form.get('bookname')
        book_author = request.form.get('bookauthor')
        book_rating = request.form.get('bookrating')
        # book_dict = {'title':f'{book_name}','author':f'{book_author}','rating':f'{book_rating}'}
        new_book = Book(title=book_name,
                        author=book_author, rating=book_rating)  # primary key field(id) optional, auto generates
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for('home'))
    return render_template('add.html')

@app.route("/rating/<int:num>", methods=['GET', 'POST'])
def chng_rating(num):
    book = db.session.query(Book).all()[num-1]
    if request.method == 'POST':
        new_rating = request.form.get('new_rating')
        book.rating = new_rating
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('rating.html',books=book)

@app.route('/delete/<int:num>')
def delete(num):
    book = db.session.query(Book).all()[num-1]
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))
    
if __name__ == "__main__":
    app.run(debug=True)
