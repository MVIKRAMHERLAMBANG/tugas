# Doctor class to represent a doctor in the hospital
class Doctor:
    def __init__(self, name, doctor_id, specialty):
        self.name = name
        self.doctor_id = doctor_id
        self.specialty = specialty

    def __str__(self):
        return f"Dr. {self.name}, {self.specialty}"