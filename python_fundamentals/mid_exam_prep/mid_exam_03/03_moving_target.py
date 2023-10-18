def shoot(some_index: int, shot_power: int, some_list: list):
    if 0 <= some_index < len(some_list):
        some_list[some_index] -= shot_power
        if some_list[some_index] <= 0:
            some_list.remove(some_list[some_index])
    return some_list


def add(some_index: int, some_value: int, some_list: list):
    if 0 <= some_index < len(some_list):
        some_list.insert(some_index, some_value)
        return some_list
    print('Invalid placement!')


def strike(some_index: int, some_radius: int, some_list: list):
    if 0 <= some_index - some_radius < some_index + some_radius < len(some_list):
        del some_list[some_index - some_radius:some_index + some_radius + 1]
        return some_list
    print('Strike missed!')


targets = [int(x) for x in input().split()]

while True:
    command = input()
    if command == 'End':
        break
    current_command = command.split()
    if current_command[0] == 'Shoot':
        index = int(current_command[1])
        power = int(current_command[2])
        shoot(index, power, targets)
    elif current_command[0] == 'Add':
        index = int(current_command[1])
        value = int(current_command[2])
        add(index, value, targets)
    elif current_command[0] == 'Strike':
        index = int(current_command[1])
        radius = int(current_command[2])
        strike(index, radius, targets)

print('|'.join(str(x) for x in targets))
