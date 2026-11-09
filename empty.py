
numbers = [1, 2, 3, 4, 5, 6]
even_squares =[(n ** 2) for n in numbers if n % 2 == 0 ]
print(even_squares)


for n in range(5, 26, 5):
    print(n)


inventory = ["Laptop", "Monitor", "Keyboard", "Mouse"]
for index,invent in enumerate(inventory, start=1):
    print (f"Aisle Slot {index}: {invent}")

students = ["Emma", "Liam", "Sophia"]
grades = ["A", "B", "A+"]
for student, grade in zip(students,grades):
    print(f'{student} received a grade of {grade}')
print('')

