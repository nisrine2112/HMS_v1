from models import db, Employee

def add_employee_services(data):
    employee = Employee(
        name=data['name'],
        age=data['age'],
        phone=data['phone'],
        address=data['address']
    )
    db.session.add(employee)
    db.session.commit()