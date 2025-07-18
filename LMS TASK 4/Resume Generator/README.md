Resume Generator
Overview
The Resume Generator is a Python-based command-line application that generates a resume from structured JSON data. It loads personal information, education, experience, and skills from a resume.json file and exports the resume in both plain text (.txt) and Markdown (.md) formats.
Features

JSON-based Input: Store resume data in a structured resume.json file.
Export Formats: Generate resumes in .txt (plain text) and .md (Markdown) formats.
Modular Design: Uses a separate formatter.py module for formatting functions.
Simple Interface: Command-line menu to choose export format or exit.

Requirements

Python 3.x
Standard library modules: json, os

Files

resume.json: JSON template storing resume data (personal info, education, experience, skills).
resume.py: Main application logic to load JSON data and handle user interaction.
formatter.py: Contains functions to format resume data into .txt and .md formats.
resume.txt: Output file for plain text resume (generated on demand).
resume.md: Output file for Markdown resume (generated on demand).

Installation

Ensure Python 3.x is installed on your system.
Clone or download the project files (resume.json, resume.py, formatter.py) to a directory.
No additional dependencies are required.

Usage

Edit resume.json to include your personal information, education, experience, and skills.
Navigate to the project directory in your terminal.
Run the application using:python resume.py


Follow the on-screen menu to:
Export as .txt: Generate resume.txt with a plain text resume.
Export as .md: Generate resume.md with a Markdown resume.
Exit: Close the application.



Example
Sample resume.json
{
    "personal_info": {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "phone": "123-456-7890",
        "address": "123 Main St, Anytown, USA"
    },
    "education": [
        {
            "degree": "Bachelor of Science in Computer Science",
            "institution": "University of Example",
            "year": "2018-2022"
        }
    ],
    "experience": [
        {
            "title": "Software Engineer",
            "company": "Tech Corp",
            "location": "Tech City, USA",
            "duration": "2022-Present",
            "responsibilities": [
                "Developed web applications using Python and JavaScript",
                "Collaborated with cross-functional teams to deliver projects"
            ]
        }
    ],
    "skills": [
        "Python",
        "JavaScript",
        "SQL",
        "Git"
    ]
}

Running the Application
=== Resume Generator ===
1. Export as .txt
2. Export as .md
3. Exit
Select an option: 1
Resume exported to resume.txt

Sample resume.txt Output
JOHN DOE
========
Email: john.doe@example.com
Phone: 123-456-7890
Address: 123 Main St, Anytown, USA

EDUCATION
---------
Bachelor of Science in Computer Science
University of Example | 2018-2022

EXPERIENCE
----------
Software Engineer | Tech Corp, Tech City, USA
2022-Present
- Developed web applications using Python and JavaScript
- Collaborated with cross-functional teams to deliver projects

SKILLS
------
Python, JavaScript, SQL, Git

Sample resume.md Output
# John Doe
**Email**: john.doe@example.com | **Phone**: 123-456-7890 | **Address**: 123 Main St, Anytown, USA

## Education
### Bachelor of Science in Computer Science
University of Example | 2018-2022

## Experience
### Software Engineer | Tech Corp, Tech City, USA
*2022-Present*
- Developed web applications using Python and JavaScript
- Collaborated with cross-functional teams to deliver projects

## Skills
Python, JavaScript, SQL, Git


Notes

Ensure resume.json is properly formatted to avoid JSON parsing errors.
The application assumes valid JSON input. Invalid JSON will cause the program to fail with an error message.
The .txt and .md outputs are overwritten each time an export is performed.
The formatter.py module separates formatting logic for reusability and clarity.

Future Improvements

Add input validation for resume.json fields (e.g., valid email, phone formats).
Support additional export formats (e.g., PDF using LaTeX).
Allow editing of resume.json through the command-line interface.
Add templates for different resume styles (e.g., academic, technical).

License
This project is open-source and available under the MIT License.