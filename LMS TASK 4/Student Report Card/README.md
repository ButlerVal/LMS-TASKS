Student Report Card App
Overview
The Student Report Card App is a Python-based command-line application designed to manage student records, including their names, subjects, scores, averages, and grades. It allows users to add, view, and update student information, with data persistently stored in a JSON file.
Features

Add Student: Input a student's name, subjects, and scores to create a new student record.
View Students: Display all student records, including their subjects, scores, average, and grade.
Update Student: Modify the scores of an existing student and recalculate their average and grade.
Data Persistence: Student data is saved to and loaded from a students.json file using JSON format.
Grade Calculation: Automatically calculates a student's average score and assigns a grade based on the following scale:
A: ≥70
B: ≥60
C: ≥50
D: ≥45
E: ≥40
F: <40



Requirements

Python 3.x
No external libraries are required beyond the standard library (json and os).

Files

main.py: Contains the core application logic, including the Student class and the main menu interface.
utils.py: Provides utility functions for saving and loading student data to/from a JSON file.
students.json: Generated automatically to store student data persistently.

Installation

Ensure Python 3.x is installed on your system.
Clone or download the project files (main.py and utils.py) to a directory.
No additional dependencies are required.

Usage

Navigate to the project directory in your terminal.
Run the application using:python main.py


Follow the on-screen menu to:
Add a student: Enter the student's name, number of subjects, subject names, and scores.
View students: See a list of all students with their details.
Update a student: Modify scores for an existing student by entering their name.
Exit: Save changes and exit the application.



Example
=== Student Report Card App ===
1. Add Student
2. View Students
3. Update Student
4. Exit
Select an option: 1
Enter student name: John Doe
Enter number of subjects: 3
Enter subject name: Math
Enter score for Math: 85
Enter subject name: English
Enter score for English: 90
Enter subject name: Science
Enter score for Science: 78
Student John Doe added successfully.

Notes

Student names and subjects are automatically capitalized, and leading/trailing whitespace is stripped.
The application handles invalid inputs gracefully (e.g., non-numeric scores will raise an error and need to be re-entered).
Data is saved to students.json after every add or update operation.
If students.json does not exist initially, it will be created automatically when a student is added.

Future Improvements

Add input validation for scores (e.g., ensure scores are between 0 and 100).
Implement a delete student feature.
Add support for editing subject names or adding/removing subjects for a student.
Include error handling for file operations and invalid JSON data.

License
This project is open-source and available under the MIT License.