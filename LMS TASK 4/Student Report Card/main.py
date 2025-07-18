class Student:
    def __init__(self, name, subjects, scores):
        self.name = name
        self.subjects = subjects 
        self.scores = scores      
        self.average = 0.0
        self.grade = ""
        self.calculate_average()
        self.assign_grade()

    def calculate_average(self):
        if self.scores:
            total = sum(self.scores)
            count = len(self.scores)
            self.average = total / count
        else:
            self.average = 0.0

    def assign_grade(self):
        avg = self.average
        if avg >= 70:
            self.grade = "A"
        elif avg >= 60:
            self.grade = "B"
        elif avg >= 50:
            self.grade = "C"
        elif avg >= 45:
            self.grade = "D"
        elif avg >= 40:
            self.grade = "E"
        else:
            self.grade = "F"

    def to_dict(self):
        return {
            "name": self.name,
            "subjects": self.subjects,
            "scores": self.scores,
            "average": self.average,
            "grade": self.grade
        }

    @staticmethod
    def from_dict(data):
        student = Student(data["name"], data["subjects"], data["scores"])
        return student