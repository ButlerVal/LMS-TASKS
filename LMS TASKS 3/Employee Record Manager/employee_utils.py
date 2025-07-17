import json
import os
from employee_main import Employee

def save_employees(employees, filename):
    employee_list = []
    for employee in employees:
        employee_list.append({
            "Name": employee.name,
            "Id": employee.id,
            "Department": employee.department,
            "Salary": employee.salary
        })
    with open(filename, 'w') as file:
        json.dump(employee_list, file, indent=4)

def load_employees(filename):
    employees = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            employee_list = json.load(file)
        for data in employee_list:
            employee = Employee(data['Name'], data['Id'], data['Department'], data['Salary'])
            employees.append(employee)
    else:
        print(f"{filename} does not exist. Starting with an empty employee list.")
    return employees        

def search_by_id(employees):
    id = input("Enter employee id to search for: ").strip()
    for employee in employees:
        if id == employee.id:
            print(employee)
            return
    print("Id is invalid")    

def add_employee(employees):
    name = input("Enter employee name: ").strip().title()
    id = input("Enter employee id: ").strip()
    department = input("Enter employee department: ").strip().capitalize()
    
    while True:
        salary = input("Enter employee salary: ").strip()
        try:
            salary = float(salary)
            break
        except ValueError:
            print("Invalid salary. Please enter a numeric value.")

    employee = Employee(name, id, department, salary)
    employees.append(employee)
    print(f"Employee {name} has been added successfully.")

def view_employees(employees):
    if not employees:
        print("No employees to display.")
    for employee in employees:
        print(employee)