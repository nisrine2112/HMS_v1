from models.models_patient import db, Patient

def add_patient_services(data):

    patient = Patient(
        name=data["name"],
        age=data["age"],
        phone=data["phone"],
        address=data["address"]
    )

    db.session.add(patient)
    db.session.commit()
