days = int(input())

money_gained = 0
total_win = 0
total_lose = 0


for day in range(days):
    current_money = 0
    win_counter = 0
    lose_counter = 0
    while True:
        command = input()
        if command == 'Finish':
            break
        result = input()
        if result == 'win':
            win_counter += 1
            current_money += 20
        elif result == 'lose':
            lose_counter += 1
    total_win += win_counter
    total_lose += lose_counter
    if win_counter > lose_counter:
        current_money *= 1.1
    money_gained += current_money

if total_win > total_lose:
    money_gained *= 1.2
    print(f'You won the tournament! Total raised money: {money_gained:.2f}')
else:
    print(f'You lost the tournament! Total raised money: {money_gained:.2f}')



