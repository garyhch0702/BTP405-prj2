from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import os

app = Flask(__name__)

uri = os.getenv("DATABASE_URL")
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Reservation(db.Model):
    __tablename__ = 'reservations'
    reservation_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    reservation_time = db.Column(db.DateTime, nullable=False)
    guests = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(50), nullable=False)

@app.route('/reservation', methods=['POST'])
def create_reservation():
    data = request.get_json()
    new_reservation_time = datetime.fromisoformat(data['reservation_time'])
    
    conflict = Reservation.query.filter(
        Reservation.reservation_time.between(new_reservation_time - timedelta(hours=2),
                                             new_reservation_time + timedelta(hours=2))
    ).first()
    if conflict:
        return jsonify({'message': 'Reservation time conflicts with an existing reservation.'}), 400
    
    reservation = Reservation(
        user_id=data['user_id'],
        reservation_time=new_reservation_time,
        guests=data['guests'],
        status=data['status']
    )
    db.session.add(reservation)
    db.session.commit()
    return jsonify({'message': 'Reservation created successfully.'}), 201

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
