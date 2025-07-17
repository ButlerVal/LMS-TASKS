student = {}

def add_student():
    name = input("What is the students name? ").strip().capitalize()
    if name in student:
        print("Student Already Exists")
        return
    scores = []
    for i in range(3):
        value = int(input(f"Enter scores {i + 1} for {name}:\n"))
        try:
            if value < 0:
                print("Score must be greater than Zero")
                return
            else:    
                scores.append(value)
        except ValueError:
            print("Invalid input. Enter a number")
            return

    student.update({name: scores})
    print(f"Student {name} added successfully!!")

def show_allStudent():
    if not student:
        print("No students yet")
        return
    for key, value in student.items():
        print(f"Student Name:", key)

        print(f"Student Scores:", value)

        average = sum(value)/len(value)

        print(f"Average Score is {average}")

        if average < 50:
            print(f"{key}'s Performance is Poor")
    
        elif average < 80:
            print(f"{key}'s Performance is Good")
    
        else:
            print(f"{key}'s performance is Excellent") 
        print()

def search_student():
    
    student_name = input("Enter the name of the student ").strip().capitalize()
    if student_name in student:
        value = student[student_name]
        print(f"Student Name:", student_name)
        print(f"Student Scores:", value)

        average = sum(value)/len(value)

        print(f"Average Score is {average}")

        if average < 50:
            print(f"{student_name}'s is Poor")
    
        elif average < 80:
            print(f"{student_name}'s Performance is Good")
    
        else:
            print(f"{student_name}'s performance is Excellent")
    else:
        print(f"Student Name {student_name}'s not found") 

    print()   

def main():
    while True:
        print("----System Menu-----")
        print("1. Add New Student")
        print("2. Show All Students")
        print("3. Search For a Student")
        print("4. Exit")

        choice = (input("Pick a number from 1-4 ").strip())
        print()

        if choice == "1":
            add_student()

        elif choice == "2":
            show_allStudent()

        elif choice == "3":
            search_student()

        elif choice == "4":
            print("Are you sure you want to exit Y/N")
            ans = input("Enter Y to stay or N to exit ").upper().strip()
            if ans == "N":
                main()
            elif ans == "Y":
                print("Goodbye! Thanks for using our student management system")
                break
            else:
                print("Invalid input. Please enter Y or N ")               
        
        else:
            print("Invalid option. Please try again.")

    

        


main()            


            
                            
        
#add_student()
#show_allStudent()            
   