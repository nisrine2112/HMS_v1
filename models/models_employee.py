from models.models_patient import db

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employeeID = db.Column(db.String(50), unique=True, nullable=False)
    fullName = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    phoneNumber = db.Column(db.String(20))
    email = db.Column(db.String(100), unique=True)
    shift = db.Column(db.String(50))