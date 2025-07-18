from utils import save_students, load_students

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
    
def add_student(students):
    name = input("Enter student name: ").capitalize().strip()
    num_subjects = int(input("Enter number of subjects: ").strip())
    subjects = []
    scores = []
    for _ in range(num_subjects):
        subject = input("Enter subject name: ").strip().capitalize()
        score = float(input(f"Enter score for {subject}: ").strip())
        subjects.append(subject)
        scores.append(score)
    student = Student(name, subjects, scores)
    students.append(student)
    print()
    print(f"Student {name} added successfully.\n")

def view_students(students):
    if not students:
        print("No students found.\n")
        return
    for idx, student in enumerate(students, start=1):
        print()
        print(f"--- Student {idx} ---")
        print(f"Name: {student.name}")
        for subj, score in zip(student.subjects, student.scores):
            print(f"{subj}: {score}")
        print(f"Average: {student.average:.2f}")
        print(f"Grade: {student.grade}")
        print()

def update_student(students):
    name = input("Enter name of student to update: ").strip().capitalize()
    for student in students:
        if student.name == name:
            print(f"Updating scores for {name}.")
            for i in range(len(student.subjects)):
                subject = student.subjects[i]
                score = float(input(f"Enter new score for {subject}: ").strip())
                student.scores[i] = score
            student.calculate_average()
            student.assign_grade()
            print(f"Student {name} updated successfully.\n")
            return
    print(f"Student {name} not found.\n")

def main():
    filename = "students.json"
    students = load_students(filename)

    while True:
        print()
        print("=== Student Report Card App ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            add_student(students)
            save_students(students, filename)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            update_student(students)
            save_students(students, filename)
        elif choice == "4":
            save_students(students, filename)
            print("Goodbye!. Thanks for using the student report card")
            break
        else:
            print("Invalid option. Please try again.\n")

if __name__ == "__main__":
    main()        