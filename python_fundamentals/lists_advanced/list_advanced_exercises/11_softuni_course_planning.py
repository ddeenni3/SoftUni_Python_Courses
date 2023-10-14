course_schedule = input().split(', ')

while True:
    command = input().split(':')
    if command[0] == 'course start':
        break
    elif command[0] == 'Add':
        lesson_title = command[1]
        if lesson_title not in course_schedule:
            course_schedule.append(lesson_title)
    elif command[0] == 'Insert':
        lesson_title = command[1]
        insert_index = int(command[2])
        if lesson_title not in course_schedule:
            course_schedule.insert(insert_index, lesson_title)
    elif command[0] == 'Remove':
        lesson_title = command[1]
        if lesson_title in course_schedule:
            while lesson_title in course_schedule:
                course_schedule.remove(lesson_title)
                if f'{lesson_title}-Exercise' in course_schedule:
                    course_schedule.remove(f'{lesson_title}-Exercise')
    elif command[0] == 'Swap':
        first_lesson = command[1]
        second_lesson = command[2]
        if first_lesson in course_schedule and second_lesson in course_schedule:
            first_index = course_schedule.index(first_lesson)
            second_index = course_schedule.index(second_lesson)
            course_schedule[first_index], course_schedule[second_index] = \
                course_schedule[second_index], course_schedule[first_index]
            if f'{first_lesson}-Exercise' in course_schedule:
                first_lesson_exercise_index = course_schedule.index(f'{first_lesson}-Exercise')
                course_schedule.remove(f'{first_lesson}-Exercise')
                course_schedule.insert(second_index + 1, f'{first_lesson}-Exercise')
            elif f'{second_lesson}-Exercise' in course_schedule:
                first_lesson_exercise_index = course_schedule.index(f'{second_lesson}-Exercise')
                course_schedule.remove(f'{second_lesson}-Exercise')
                course_schedule.insert(first_index + 1, f'{second_lesson}-Exercise')
    elif command[0] == 'Exercise':
        lesson_title = command[1]
        if lesson_title not in course_schedule:
            course_schedule.append(lesson_title)
            course_schedule.append(f'{lesson_title}-Exercise')
        else:
            if lesson_title in course_schedule and f'{lesson_title}-Exercise' not in course_schedule:
                lesson_index = course_schedule.index(lesson_title)
                course_schedule.insert(lesson_index + 1, f'{lesson_title}-Exercise')
for lesson in range(1, len(course_schedule) + 1):
    print(f'{lesson}.{course_schedule[lesson-1]}')
