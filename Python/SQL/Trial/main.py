# import sqlite3


# db = sqlite3.connect("books-collection.db")

# cursor = db.cursor()

# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy


# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
# # db.create_all()


# class Book(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(250), unique=True, nullable=False)
#     author = db.Column(db.String(250), nullable=False)
#     rating = db.Column(db.Float, nullable=False)

#     def __repr__(self):
#         return f'<Book {self.title}>'


# # db.create_all()

# # new_book = Book(title='Harry Potter',
# #              author='J. K. Rowling', rating=9.3) #primary key field(id) optional, auto generates
# # db.session.add(new_book)
# # db.session.commit()

# all_books = Book.all()

# print(all_books)
import email
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///username-passwrd.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

# db.create_all()

# admin = User(username='admin', email='admin@example.com')
# guest = User(username='guest', email='guest@example.com')
# don = User(username='don', email='don@example.com')
# db.session.add(admin)
# db.session.add(don)
# db.session.commit()

data = User.query.all()
print(data[0].email)