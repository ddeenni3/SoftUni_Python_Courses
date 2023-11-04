programs = {}


while True:
    command = input()
    if command == 'end':
        break
    course, name = command.split(' : ')
    if course not in programs.keys():
        programs[course] = [name]
    else:
        programs[course].append(name)

for course, students in programs.items():
    registered_students = len(programs[course])
    print(f'{course}: {registered_students}')
    for student in students:
        print(f'-- {student}')

