judges_amount = int(input())

presentation = input()

total_grades = 0
grades_counter = 0

while presentation != 'Finish':
    average_grade = 0
    for i in range(judges_amount):
        grade = float(input())
        average_grade += grade
        total_grades += grade
        grades_counter += 1
    print(f'{presentation} - {average_grade / judges_amount:.2f}.')
    presentation = input()

print(f'Student\'s final assessment is {total_grades / grades_counter:.2f}.')
