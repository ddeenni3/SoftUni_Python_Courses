from collections import deque

water_quantity = int(input())

name = input()

people = deque()

while name != 'Start':
    people.append(name)
    name = input()

command = input()

while command != 'End':
    actions = command.split()
    if len(actions) == 1:
        liters = int(actions[0])
        if water_quantity >= liters:
            print(f'{people.popleft()} got water')
            water_quantity -= liters
        else:
            print(f'{people.popleft()} must wait')
    else:
        liters = int(actions[1])
        water_quantity += liters
    command = input()

print(f'{water_quantity} liters left')
