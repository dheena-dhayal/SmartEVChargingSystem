from database import db

class Station(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    max_power_kw = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='Available')  # Available, Maintenance, Occupied
    location = db.Column(db.String(100), default='Unknown')
    
    bookings = db.relationship('Booking', backref='station', lazy='dynamic')
