from department import Department

class HospitalQueue:
    def __init__(self):
        self.departments = []

    def Show(self):
        print("Hospital Queue Management:")
        options = [
            '1) Add new patient',
            '2) View patients in a department ["Cardiology", "Orthopedics", "Pediatrics", "Neurology", "Dermatology"]',
            '3) Call the next patient',
            '4) Remove patient',
            '5) Exit'
        ]
        for option in options:
            print(option)
        return ValidateInput("Choose an option (1-5): ", [1, 2, 3, 4, 5])

    def run(self):
        while True:
            choice = self.Show()

            if choice == 1:
                DepName = input("Enter department name: ")
                PatName = input("Enter patient name: ")
                try:
                    urgency = int(input("Enter urgency level (0: Normal, 1: Urgent, 2: Emergency): "))
                except ValueError:
                    print("Invalid urgency level. Please enter a number (0-2).")
                    continue
                department = self.LookOrCreateDepartment(DepName)
                department.AddPatient(PatName, urgency)

            elif choice == 2:
                DepName = input("Enter department name: ")
                department = self.LookForDepartment(DepName)
                if department:
                    department.ShowQueue()
                else:
                    print("Department not found!")

            elif choice == 3:
                DepName = input("Enter department name: ")
                department = self.LookForDepartment(DepName)
                if department:
                    department.NextPatient()
                else:
                    print("Department not found!")

            elif choice == 4:
                DepName = input("Enter department name: ")
                PatName = input("Enter patient name to remove: ")
                department = self.LookForDepartment(DepName)
                if department:
                    department.DeletePatient(PatName)
                else:
                    print("Department not found!")

            elif choice == 5:
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")
    def LookOrCreateDepartment(self, name):
        for dept in self.departments:
            if dept.name == name:
                return dept
        new_dept = Department(name)
        self.departments.append(new_dept)
        return new_dept

    def LookForDepartment(self, name):
        for dept in self.departments:
            if dept.name == name:
                return dept
        return None
    
def ValidateInput(prompt, valid_options):
    while True:
        user_input = input(prompt)
        if not user_input.isdigit():
            print("Please enter a valid number.")
            continue
        user_input = int(user_input)
        if user_input in valid_options:
            return user_input
        else:
            options_str = ""  
            for i in range(len(valid_options)):  
                if i == 0:  
                    options_str += str(valid_options[i])  
                else:  
                    options_str += ", " + str(valid_options[i])  

            print("Please enter a valid option: " + options_str)