count_even = 0
count_odd = 0
count_negative = 0
count_zero = 0

for num in range(5):
    num = int(input("Enter number for analysis"))
    if num % 2 == 0:
        print(f"{num} is Even")
        count_even+=1
    else:
        print(f"{num} is Odd")
        count_odd+=1

    if num > 0:
        print(f"{num} is Positive")
    elif num == 0:
        print(f"{num} is Zero")
        count_zero+=1
    else:
        print(f"{num} is Negative")
        count_negative+=1

print(f"Even Numbers: {count_even}")
print(f"Odd Numbers: {count_odd}")
print(f"Zero: {count_zero}")
print(f"Negative Numbers: {count_negative}")  
      




