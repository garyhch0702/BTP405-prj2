import os
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/restaurant_reservation_system'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model
class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

# Authentication
users = {
    "admin": "password",
}

@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return username

# UserResource endpoint for creating a user
@app.route('/')
def index():
    return 'Welcome to the Restaurant Reservation System!'
@app.route('/user', methods=['POST'])
@auth.login_required
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
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)
