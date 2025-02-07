from department import Department
from random import randint
from hospital import HospitalQueue

def GenerateData(assignment):
    departments = ["Cardiology", "Orthopedics", "Pediatrics", "Neurology", "Dermatology"]
    Prename = ["Amin", "Ramzi", "Carlos", "Jordi", "Alex", "Emma", "Lucas", "Louis", "Iker", "Thomas"]
    Name = ["Modric", "Ancelotti", "Casillas", "Morel", "Alba", "Bernard", "Martin", "Garcia", "Davis", "Rodriguez"]
    for DepName in departments:
        department = Department(DepName)
        for j in range(3):
            n = randint(0, 9)
            l = randint(0, 9)
            PatName = f"Patient {Prename[n]} {Name[l]}"
            urgency = randint(0, 2)
            department.AddPatient(PatName, urgency)
        assignment.departments.append(department)

if __name__ == '__main__':
    assignment = HospitalQueue()
    GenerateData(assignment)
    assignment.run()