total_goals = 0
best_player = 0
hat_trick = False

while True:
    current_goals = 0
    command = input()
    if command == "END":
        break
    goals = int(input())
    current_goals += goals
    if current_goals > total_goals:
        total_goals = current_goals
        best_player = command
        if goals >= 3:
            hat_trick = True
    if goals >= 10:
        print(f'')
        break


print(f'{best_player} is the best player!')

if hat_trick:
    print(f'He has scored {total_goals} goals and made a hat-trick !!!')
else:
    print(f'He has scored {total_goals} goals.')
