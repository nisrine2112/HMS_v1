from models.models_medicine import Medicine
from models.models_patient import db

def add_medicine_services(data):
    from datetime import date
    new_medicine = Medicine(
        name        = data["name"],
        quantity    = data["quantity"],
        expiry_date = data["expiry_date"],
        unit_price  = data["unit_price"]
    )
    db.session.add(new_medicine)
    db.session.commit()
