number_of_students = int(input())

students = {}

for _ in range(number_of_students):
    name, grade = input().split()
    if name not in students.keys():
        students[name] = []
    students[name].append(float(grade))

for student, grade in students.items():
    average_grade = sum(grade) / len(grade)
    formatted_grade = f'{" ".join([f"{g:.2f}" for g in grade])}'
    print(f'{student} -> {formatted_grade} (avg: {average_grade:.2f})')