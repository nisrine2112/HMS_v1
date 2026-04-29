from flask import Flask, render_template, request
from models import db, Patient, Employee
from services import add_patient_services, add_employee_services

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hospital.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def base():
    return render_template("base.html")

@app.route('/add_patient', methods=["GET", "POST"])
def add_patient():
    if request.method == "POST":
        data = {
            "name": request.form["name"],
            "age": request.form["age"],
            "phone": request.form["phone"],
            "address": request.form["address"]
        }

        add_patient_services(data)
        return "Data SAVED SUCCESSFULLY"

    return render_template("add_patient.html")

@app.route('/view_update_patient')
def view_update_patient():
    patients = Patient.query.all()
    return render_template("view_update_patient.html", patients=patients)

@app.route('/edit_patient/<int:id>', methods=["GET", "POST"])
def edit_patient(id):
    patient = Patient.query.get(id)
    if request.method == "POST":
        patient.name = request.form["name"]
        patient.age = request.form["age"]
        patient.phone = request.form["phone"]
        patient.address = request.form["address"]

        db.session.commit()
        return "Data Updated Successfully"
    return render_template("edit_patient.html", patient=patient)




@app.route('/add_employee', methods=["GET", "POST"])
def add_employee():
    if request.method == "POST":
        data = {
            "name": request.form["name"],
            "age": request.form["age"],
            "phone": request.form["phone"],
            "address": request.form["address"]
        }

        add_employee_services(data)
        return "Data SAVED SUCCESSFULLY"

    return render_template("add_employee.html")

@app.route('/view_update_employee')
def view_update_employee():
    employees = Employee.query.all()
    return render_template("view_update_employee.html", employees=employees)

@app.route('/edit_employee/<int:id>', methods=["GET", "POST"])
def edit_employee(id):
    employee = Employee.query.get(id)
    if request.method == "POST":
        employee.name = request.form["name"]
        employee.age = request.form["age"]
        employee.phone = request.form["phone"]
        employee.address = request.form["address"]

        db.session.commit()
        return "Data Updated Successfully"
    return render_template("edit_employee.html", employee=employee)

if __name__ == '__main__':
    app.run(debug=True)