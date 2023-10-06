card_sequence = input()
card_sequence = card_sequence.split(' ')

team_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_b = team_a.copy()
is_terminated = False

for card in card_sequence:
    card_list = card.split('-')
    if card_list[0] == 'A':
        if int(card_list[1]) in team_a:
            team_a.remove(int(card_list[1]))
    elif card_list[0] == 'B':
        if int(card_list[1]) in team_b:
            team_b.remove(int(card_list[1]))
    if len(team_a) < 7 or len(team_b) < 7:
        is_terminated = True
        break

print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')
if is_terminated:
    print('Game was terminated')
