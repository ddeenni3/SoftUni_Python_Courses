from math import ceil

number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus_points = int(input())

max_bonus = 0
max_attendance = 0

for student in range(number_of_students):
    current_student_attendance = int(input())
    current_student_score = current_student_attendance / number_of_lectures * (5 + additional_bonus_points)
    if current_student_score > max_bonus:
        max_bonus = current_student_score
        max_attendance = current_student_attendance

print(f'Max Bonus: {ceil(max_bonus)}.\nThe student has attended {max_attendance} lectures.')
