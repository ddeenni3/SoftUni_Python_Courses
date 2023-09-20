students_amount = int(input())

total_grade = 0
top = 0
between4_5 = 0
between3_4 = 0
fail = 0


for students in range(students_amount):
    grade = float(input())
    total_grade += grade
    if grade >= 5:
        top += 1
    elif 4 <= grade <= 4.99:
        between4_5 += 1
    elif 3 <= grade <= 3.99:
        between3_4 += 1
    elif grade < 3:
        fail += 1
print(f'Top students: {top / students_amount * 100:.2f}%')
print(f'Between 4.00 and 4.99: {between4_5 / students_amount * 100:.2f}%')
print(f'Between 3.00 and 3.99: {between3_4 / students_amount * 100:.2f}%')
print(f'Fail: {fail / students_amount * 100:.2f}%')
print(f'Average: {total_grade / students_amount:.2f}')
