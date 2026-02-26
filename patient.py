# Patient class to represent a patient
class Patient:
    def __init__(self, name, patient_id):
        self.name = name
        self.patient_id = patient_id
        self.appointments = []

    def make_appointment(self, doctor, appointment_date):
        appointment = Appointment(self, doctor, appointment_date)
        self.appointments.append(appointment)
        print(f"Appointment made for {self.name} with {doctor.name} on {appointment_date}")