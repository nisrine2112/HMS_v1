from models.models_patient import db

class Attendance(db.Model):
    id              = db.Column(db.Integer, primary_key=True)
    date            = db.Column(db.Date)
    check_in_time   = db.Column(db.Time)
    check_out_time  = db.Column(db.Time)
    status          = db.Column(db.String(50))
