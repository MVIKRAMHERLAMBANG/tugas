# Appointment class to represent an appointment between a patient and a doctor
class Appointment:
    def __init__(self, patient, doctor, appointment_date):
        self.patient = patient
        self.doctor = doctor
        self.appointment_date = appointment_date
        self.treatments = []

    def add_treatment(self, treatment_name, treatment_date):
        treatment = Treatment(self, treatment_name, treatment_date)
        self.treatments.append(treatment)
        print(f"Treatment '{treatment_name}' added for appointment on {self.appointment_date}")