failed_max_amount = int(input())

command = input()


expelled = False

last_problem = ''
failed = 0
problems_counter = 0
total_score = 0

while command != "Enough":
    score = int(input())
    last_problem = command
    problems_counter += 1
    total_score += score
    if score <= 4:
        failed += 1
        if failed >= failed_max_amount:
            expelled = True
            print(f'You need a break, {failed} poor grades.')
            break
    command = input()


if not expelled:
    print(f'Average score: {total_score / problems_counter:.2f}')
    print(f'Number of problems: {problems_counter}')
    print(f'Last problem: {last_problem}')








