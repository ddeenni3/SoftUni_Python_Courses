initial_energy = int(input())
win_counter = 0
battle_won = True

while initial_energy >= 0:
    command = input()
    if command == 'End of battle':
        break
    distance = int(command)
    if initial_energy - distance >= 0:
        win_counter += 1
        initial_energy -= distance
        if win_counter % 3 == 0:
            initial_energy += win_counter
    else:
        battle_won = False
        break
if battle_won:
    print(f'Won battles: {win_counter}. Energy left: {initial_energy}')
else:
    print(f'Not enough energy! Game ends with {win_counter} won battles and {initial_energy} energy')
