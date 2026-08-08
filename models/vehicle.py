from database import db

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    model = db.Column(db.String(64), nullable=False)
    battery_capacity = db.Column(db.Float, nullable=False)  # in kWh
    current_charge = db.Column(db.Float, default=0.0)  # in %
    
    bookings = db.relationship('Booking', backref='vehicle', lazy='dynamic')
