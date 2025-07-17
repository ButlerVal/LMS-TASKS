num_of_students = int(input("How many Students are in the class?"))

count_fail = 0
count_pass = 0
count_excellent = 0

for i in range(num_of_students):

    student_name = input("What's the students name?")
    score1 = float(input("What's is the stdents score"))
    score2 = float(input("What's is the stdents score"))
    score3 = float(input("What's is the stdents score"))
    average = (score1 + score2 + score3)/3

    if average < 50:
        result = "Fail"
        count_fail +=1

    elif average < 80:
        result = "Pass"
        count_pass +=1
    else:
        result = "Excellent"  
        count_excellent +=1  

print("------- Result Summary ---------")
print(f"Failed: {count_fail}")
print(f"Passed: {count_pass}")
print(f"Excellent: {count_excellent}")

               