import os
import json

def save_students(students, filename):
    data = [s.to_dict() for s in students]
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def load_students(filename):
    from main import Student
    students = []
    if os.path.exists(filename):
        with open(filename, "r") as f:
            data = json.load(f)
            students = [Student.from_dict(d) for d in data]
    return students