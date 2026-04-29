from models.models_attendance import Attendance
from models.models_patient import db

def add_attendance_services(data):
    new_attendance = Attendance(
        date           = data["date"],
        check_in_time  = data["check_in_time"],
        check_out_time = data["check_out_time"],
        status         = data["status"]
    )
    db.session.add(new_attendance)
    db.session.commit()
