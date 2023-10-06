first_line = input().split()
second_line = input().split()
third_line = input().split()

winning_combo_found = False
winning_player = ''
diagonal_one = [first_line[0], second_line[1], third_line[2]]
diagonal_two = [first_line[2], second_line[1], third_line[0]]
for player in range(1, 3):
    current_player = str(player)
    winning_line = [current_player, current_player, current_player]
    if winning_line == first_line or winning_line == second_line or winning_line == third_line:
        winning_player = current_player
        winning_combo_found = True
        break
    for symbol in range(0, 3):
        if first_line[symbol] == current_player and\
                second_line[symbol] == current_player and\
                third_line[symbol] == current_player:
            winning_combo_found = True
            winning_player = current_player
            break
    if diagonal_one == winning_line:
        winning_combo_found = True
        winning_player = current_player
        break
    elif diagonal_two == winning_line:
        winning_combo_found = True
        winning_player = current_player
        break

if winning_combo_found:
    if winning_player == '1':
        winning_player = 'First'
    else:
        winning_player = 'Second'
    print(f'{winning_player} player won')
else:
    print('Draw!')

