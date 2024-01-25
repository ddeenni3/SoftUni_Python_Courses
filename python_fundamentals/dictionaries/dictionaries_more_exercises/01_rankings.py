contests = {}

while True:
    command = input()
    if command == 'end of contests':
        break
    contest, password = command.split(':')
    contests[contest] = password

submissions = {}

while True:
    command = input()
    if command == 'end of submissions':
        break
    current_contest, current_password, name, points = command.split('=>')
    points = int(points)
    for contest, password in contests.items():
        if contest == current_contest and password == current_password:
            if name not in submissions.keys():
                submissions[name] = {current_contest: points}
            else:
                if current_contest not in submissions[name].keys():
                    submissions[name][current_contest] = points
                else:
                    if submissions[name][current_contest] < points:
                        submissions[name][current_contest] = points

best_student = ''
highest_score = 0

for name, submission in submissions.items():
    score = 0
    for course, points in submission.items():
        score += points
    if score > highest_score:
        best_student = name
        highest_score = score

sorted_submissions = dict(sorted(submissions.items()))
sorted_submissions = {key: dict(sorted(val.items(), reverse=True, key=lambda x: x[1]))
                      for key, val in sorted_submissions.items()}

print(f'Best candidate is {best_student} with total {highest_score} points.')
print('Ranking:')
for name, submission in sorted_submissions.items():
    print(name)
    for contest, points in submission.items():
        print(f'#  {contest} -> {points}')
