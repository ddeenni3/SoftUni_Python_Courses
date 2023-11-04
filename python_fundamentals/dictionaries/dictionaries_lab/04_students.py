students = {}

while True:
    command = input()
    if ':' not in command:
        course_to_search = ' '.join(command.split('_'))
        break
    student, student_id, course = command.split(':')
    students[student_id] = {student: course}

for current_student_id, current_student_name in students.items():
    for student_name, current_course in current_student_name.items():
        if course_to_search == current_course:
            curr_student_id = current_student_id
            curr_student_name = student_name
            print(f'{curr_student_name} - {curr_student_id}')
