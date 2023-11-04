results = {}
submissions = {}
while True:
    command = input()
    if command == 'exam finished':
        break
    current_student_info = command.split('-')
    name = current_student_info[0]
    if current_student_info[1] == 'banned':
        results.pop(name)
        continue
    language = current_student_info[1]
    points = int(current_student_info[2])
    if name in results.keys():
        if language in results[name].keys():
            if results[name][language] < points:
                results[name][language] = points
        else:
            results[name][language] = points
    else:
        results[name] = {language: points}
    if language not in submissions.keys():
        submissions[language] = 0
    submissions[language] += 1

print('Results:')
for current_student, current_results in results.items():
    for language, result in current_results.items():
        print(f'{current_student} | {result}')
print('Submissions:')
for language, submissions_amount in submissions.items():
    print(f'{language} - {submissions_amount}')
