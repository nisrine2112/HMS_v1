from models.models_patient import db

class Medicine(db.Model):
    id           = db.Column(db.Integer, primary_key=True)
    name         = db.Column(db.String(100))
    quantity     = db.Column(db.Integer)
    expiry_date  = db.Column(db.Date)
    unit_price   = db.Column(db.Float)