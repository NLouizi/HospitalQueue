from patient import Patient

class Department:
    capacity = 10
    ValidStatus = [0, 1, 2]

    def __init__(self, name):
        self.name = name
        self.queue = []

    def AddPatient(self, name, status):
        if status not in self.ValidStatus:
            print("Invalid status. Please enter a valid urgency level (0: Normal, 1: Urgent, 2: Emergency).")
            return
        if len(self.queue) >= self.capacity:
            print("The department queue is full. Cannot add more patients.")
            return
        new_patient = Patient(name, status)
        index = 0
        while index < len(self.queue) and self.queue[index].status >= status:
            index += 1
        self.queue.insert(index, new_patient)
        print(f"Patient {name} added with urgency level: {new_patient.ShowStatus()}.")

    def NextPatient(self):
        if not self.queue:
            print("No patients in the queue.")
            return
        next_patient = self.queue.pop(0)
        print(f"Calling {next_patient.name} to proceed with treatment.")

    def DeletePatient(self, name):
        patient = next((p for p in self.queue if p.name == name), None)
        if patient:
            self.queue.remove(patient)
            print(f"{name} has been removed from the queue.")
        else:
            print("Patient not found.")

    def ShowQueue(self):
        if not self.queue:
            print("No patients in the queue.")
            return
        for patient in self.queue:
            print(patient)

    def __str__(self):
        return f"{self.name}: {len(self.queue)} patients"