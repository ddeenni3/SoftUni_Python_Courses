initial_energy = 100
initial_coins = 100

current_energy = initial_energy

working_day_events = input().split('|')

for event in working_day_events:
    current_event = event.split('-')
    current_command = current_event[0]
    amount = int(current_event[1])
    if current_command == 'rest':
        gained_energy = 0
        if current_energy + amount >= initial_energy:
            gained_energy += initial_energy - current_energy
            current_energy = initial_energy
        else:
            current_energy += amount
            gained_energy += amount
        print(f'You gained {gained_energy} energy.')
        print(f'Current energy: {current_energy}.')
    elif current_command == 'order':
        if current_energy - 30 >= 0:
            current_energy -= 30
            initial_coins += amount
            print(f'You earned {amount} coins.')
        else:
            current_energy += 50
            print('You had to rest!')
    else:
        if initial_coins - amount >= 0:
            initial_coins -= amount
            print(f'You bought {current_command}.')
        else:
            print(f'Closed! Cannot afford {current_command}.')
            break
else:
    print(f'Day completed!')
    print(f'Coins: {initial_coins}')
    print(f'Energy: {current_energy}')
