jury_count = int(input())
presentation = input()

total_score = 0
grades_counter = 0

while presentation != 'Finish':
    current_average = 0
    for i in range(jury_count):
        score = float(input())
        total_score += score
        current_average += score
        grades_counter += 1

    print(f'{presentation} - {current_average / jury_count:.2f}.')
    presentation = input()

print(f'Student\'s final assessment is {total_score / grades_counter:.2f}.')
