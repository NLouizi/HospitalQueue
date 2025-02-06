class Patient:
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def ShowStatus(self):
        if self.status == 0:
            return "Normal"
        elif self.status == 1:
            return "Urgent"
        return "Emergency"

    def __str__(self):
        return f"{self.name} (Urgency: {self.ShowStatus()})"

    