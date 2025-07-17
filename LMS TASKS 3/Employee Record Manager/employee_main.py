import employee_utils

class Employee:
    def __init__(self, name, id, department, salary):
        self.name = name
        self.id = id
        self.department = department
        self.salary = float(salary)

    def __str__(self):
        return f"Name: {self.name}, Id: {self.id}, Department: {self.department}, Salary: {self.salary}"

def main():
    employees = []
    filename = "employee_data.json"

    while True:
        print("\n----Record Manager Menu-----")
        print("1. Add Employee")
        print("2. View all Employees")
        print("3. Search by Id")
        print("4. Save to file")
        print("5. Load from file")
        print("6. Exit")

        choice = input("Pick a number from 1-6: ").strip()
        print()

        if choice == "1":
            employee_utils.add_employee(employees)

        elif choice == "2":
            employee_utils.view_employees(employees)

        elif choice == "3":
            employee_utils.search_by_id(employees)

        elif choice == "4":
            employee_utils.save_employees(employees, filename)
            print("Employees have been saved to file successfully.")

        elif choice == "5":
            employees = employee_utils.load_employees(filename)
            print("Employees have been loaded from file successfully.")

        elif choice == "6":
            print("Goodbye, thanks for using our Employee record system.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()