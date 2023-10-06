initial_energy = 100
initial_coins = 100

current_energy = initial_energy
current_coins = initial_coins

events_for_the_day = input().split('|')

for event in events_for_the_day:
    current_event = event.split('-')
    event_name = current_event[0]
    event_number = int(current_event[1])
    if event_name == 'rest':
        event_energy = 0
        if current_energy + event_number <= initial_energy:
            event_energy = event_number
            print(f'You gained {event_energy} energy.')
        else:
            event_energy = initial_energy - current_energy
            print(f'You gained {event_energy} energy.')
        current_energy += event_energy
        print(f'Current energy: {current_energy}.')
    elif event_name == 'order':
        if current_energy - 30 >= 0:
            current_energy -= 30
            current_coins += event_number
            print(f'You earned {event_number} coins.')
        else:
            current_energy += 50
            print('You had to rest!')
    else:
        if current_coins - event_number >= 0:
            current_coins -= event_number
            print(f'You bought {event_name}.')
        else:
            print(f'Closed! Cannot afford {event_name}.')
            break
else:
    print('Day completed!')
    print(f'Coins: {current_coins}')
    print(f'Energy: {current_energy}')
