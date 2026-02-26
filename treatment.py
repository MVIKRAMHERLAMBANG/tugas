# Treatment class to represent a treatment provided during an appointment
class Treatment:
    def __init__(self, appointment, treatment_name, treatment_date):
        self.appointment = appointment
        self.treatment_name = treatment_name
        self.treatment_date = treatment_date

    def __str__(self):
        return f"Treatment: {self.treatment_name} on {self.treatment_date}"