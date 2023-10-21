def is_index_valid(some_index: int, some_list: list):
    return some_index in range(len(some_list))


def fire(some_list: list, some_index: int, some_damage: int):
    some_list[some_index] -= some_damage
    if some_list[some_index] <= 0:
        print('You won! The enemy ship has sunken.')
        exit()
    return some_list


def defend(starting_index: int, ending_index: int, some_damage: int, some_list: list):
    for i in range(starting_index, ending_index + 1):
        some_list[i] -= some_damage
        if some_list[i] <= 0:
            print('You lost! The pirate ship has sunken.')
            exit()
    return some_list


def repair(some_index: int, some_health: int, some_list: list):
    some_list[some_index] += some_health
    if some_list[some_index] > section_max_health:
        some_list[some_index] = section_max_health


pirate_ship_status = [int(x) for x in input().split('>')]
war_ship_status = [int(x) for x in input().split('>')]
section_max_health = int(input())

while True:
    command = input()
    if command == 'Retire':
        break
    current_command = command.split()
    if current_command[0] == 'Fire':
        index = int(current_command[1])
        damage = int(current_command[2])
        if is_index_valid(index, war_ship_status):
            fire(war_ship_status, index, damage)
    elif current_command[0] == 'Defend':
        start_index = int(current_command[1])
        end_index = int(current_command[2])
        damage = int(current_command[3])
        if is_index_valid(start_index, pirate_ship_status) and is_index_valid(end_index, pirate_ship_status):
            defend(start_index, end_index, damage, pirate_ship_status)
    elif current_command[0] == 'Repair':
        index = int(current_command[1])
        health = int(current_command[2])
        if is_index_valid(index, pirate_ship_status):
            repair(index, health, pirate_ship_status)
    elif current_command[0] == 'Status':
        status = [x for x in pirate_ship_status if x < (section_max_health * 0.2)]
        print(f'{len(status)} sections need repair.')

print(f'Pirate ship status: {sum(pirate_ship_status)}\nWarship status: {sum(war_ship_status)}')
