needed_hearts_per_house = [int(x) for x in input().split('@')]

last_visited_index = 0

while True:
    command = input()
    if command == 'Love!':
        break
    current_command = command.split()
    jump_length = int(current_command[1])
    visiting_index = last_visited_index + jump_length
    if last_visited_index + jump_length >= len(needed_hearts_per_house):
        visiting_index = 0
    if needed_hearts_per_house[visiting_index] - 2 >= 0:
        needed_hearts_per_house[visiting_index] -= 2
        if needed_hearts_per_house[visiting_index] == 0:
            print(f'Place {visiting_index} has Valentine\'s day.')
    else:
        needed_hearts_per_house[visiting_index] = 0
        print(f'Place {visiting_index} already had Valentine\'s day.')
    last_visited_index = visiting_index


print(f'Cupid\'s last position was {last_visited_index}.')
if sum(needed_hearts_per_house) == 0:
    print('Mission was successful.')
else:
    needed_hearts_per_house = [x for x in needed_hearts_per_house if x > 0]
    print(f'Cupid has failed {len(needed_hearts_per_house)} places.')
