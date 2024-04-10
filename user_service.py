from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
auth = HTTPBasicAuth()

uri = os.getenv("DATABASE_URL")
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

users = {"admin": "password"}

@auth.verify_password
def verify_password(username, password):
    return username in users and users[username] == password

@app.route('/')
def index():
    return 'Welcome to the Restaurant Reservation System!'

@app.route('/user', methods=['POST'])

def create_user():
    data = request.get_json()
    if not data.get('name') or not data.get('email'):
        return jsonify({'message': 'Name and email are required'}), 400
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'Email already exists'}), 400
    user = User(name=data['name'], email=data['email'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'user_id': user.user_id, 'name': user.name, 'email': user.email}), 201

if __name__ == '__main__':
    db.create_all(app=app)
    app.run(debug=True)

