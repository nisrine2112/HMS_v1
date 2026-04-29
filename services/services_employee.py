from models import db, Employee

def add_employee_services(data):
    employee = Employee(
        employeeID=data['employeeID'],
        fullName=data['fullName'],
        role=data['role'],
        phoneNumber=data['phoneNumber'],
        email=data['email'],
        shift=data['shift']
    )
    db.session.add(employee)
    db.session.commit()