player_name = input()
winner_points = 0
current_winner = None

while player_name != 'Stop':
    points = 0
    for char in range(len(player_name)):
        number = int(input())
        current_char = player_name[char]
        if number == ord(current_char):
            points += 10
        else:
            points += 2
    if points >= winner_points:
        winner_points = points
        current_winner = player_name
    player_name = input()

print(f'The winner is {current_winner} with {winner_points} points!')

