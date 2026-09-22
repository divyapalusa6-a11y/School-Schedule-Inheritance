from .student import Student

class MiddleSchoolStudent(Student):
    def __init__(self, name, grade, classes, gets_transportation=False):
        super().__init__(name, grade, classes)
        self.gets_transportation = gets_transportation

    def summary(self):
        student_summary = super().summary()
        transportation_message = self.display_transportation_message()
        return "\n".join((student_summary,transportation_message))

    def display_transportation_message(self):
        has_message = "has" if self.gets_transportation else "doesn't have"
        return f"{self.name} {has_message} transportation."

        



