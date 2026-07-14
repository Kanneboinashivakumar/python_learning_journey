class Attendance:

    def __init__(self):
        self.working_days = 30
        self.present_days = 0

    def mark_attendance(self):

        self.present_days = int(input("Enter Present Days: "))

        if self.present_days < 0 or self.present_days > self.working_days:
            raise ValueError("Invalid attendance.")

    def attendance_percentage(self):

        return (self.present_days / self.working_days) * 100

    def display(self):

        print(f"Attendance : {self.present_days}/{self.working_days}")
        print(f"Percentage : {self.attendance_percentage():.2f}%")