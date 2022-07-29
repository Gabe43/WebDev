from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random as ran
app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random", methods=['GET'])
def random():
    data = Cafe.query.all()
    num = ran.randint(0, len(data))
    return jsonify(cafe={'name': data[num].name, 'map': data[num].map_url, 'image': data[num].img_url, 'location': data[num].location, 'socket': data[num].has_sockets, 'toilet': data[num].has_toilet, 'wifi': data[num].has_wifi, 'take_calls': data[num].can_take_calls, 'seats': data[num].seats, 'price': data[num].coffee_price})


@app.route("/all", methods=['GET'])
def all():
    cafes = Cafe.query.all()
    return jsonify(cafe=[{'name': item.name, 'map': item.map_url, 'image': item.img_url, 'location': item.location, 'socket': item.has_sockets, 'toilet': item.has_toilet, 'wifi': item.has_wifi, 'take_calls': item.can_take_calls, 'seats': item.seats, 'price': item.coffee_price} for item in cafes])


@app.route("/search/<loc>", methods=['GET', 'POST'])
def search(loc):
    cafes = Cafe.query.filter_by(location=loc).all()
    if len(cafes) == 0:
        return jsonify({'error': {'Not Found': "Sorry, we don't have a cafe at this location"}})
    else:
        return jsonify(cafe=[{'name': item.name, 'map': item.map_url, 'image': item.img_url, 'location': item.location, 'socket': item.has_sockets, 'toilet': item.has_toilet, 'wifi': item.has_wifi, 'take_calls': item.can_take_calls, 'seats': item.seats, 'price': item.coffee_price} for item in cafes])


@app.route('/add', methods=['GET', 'POST'])
def add():
    new_cafe = Cafe(name=request.form.get('name'),
        map_url=request.form.get('map_url'),
        img_url=request.form.get('img_url'),
        location=request.form.get('location'),
        seats=request.form.get('seats'),
        has_toilet=bool(request.form.get('has_toilet')),
        has_wifi=bool(request.form.get('has_wifi')),
        has_sockets=bool(request.form.get('has_socket')),
        can_take_calls=bool(request.form.get('can_take_calls')),
        coffee_price=request.form.get('coffee_price'))        
    
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify({"response": {"success": "Successfully added the new cafe"}})

# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["POST","PATCH","GET"])
def patch_new_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = Cafe.query.filter_by(id=cafe_id).all()[0]
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."})
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."})

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
