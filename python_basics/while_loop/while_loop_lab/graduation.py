student_name = input()

year_passed = 0
annual_grades_total = 0
failed = 0

while year_passed < 12:
    grade = float(input())
    if grade >= 4:
        year_passed += 1
        annual_grades_total += grade
        continue
    else:
        failed += 1
        if failed == 2:
            print(f'{student_name} has been excluded at {year_passed + 1} grade')
            break
if year_passed == 12:
    print(f'{student_name} graduated. Average grade: {annual_grades_total / 12:.2f}')