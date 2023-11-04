number_of_students = int(input())
graded_students = {}

for current_student in range(number_of_students):
    student, grade = input(), float(input())
    if student not in graded_students.keys():
        graded_students[student] = [grade]
    else:
        graded_students[student].append(grade)


for student, grades in graded_students.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.50:
        graded_students[student] = average_grade
        print(f'{student} -> {average_grade:.2f}')
