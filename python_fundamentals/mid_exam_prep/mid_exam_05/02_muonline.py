def potion(some_starting_hp: int, some_initial_health: int, potion_health_amount: int):
    healed_amount = 0
    if some_starting_hp + potion_health_amount > 100:
        healed_amount = some_initial_health - some_starting_hp
        some_starting_hp = 100
    else:
        some_starting_hp += potion_health_amount
        healed_amount = potion_health_amount
    return some_starting_hp, healed_amount


def damage(starting_hp: int, damage_amount: int,):
    if starting_hp - damage_amount > 0:
        starting_hp -= damage_amount
    else:
        starting_hp = 0
    return starting_hp


dungeon = input().split('|')

initial_health = 100
current_hp = initial_health
initial_bitcoin = 0

for room in range(1, len(dungeon) + 1):
    command = dungeon[room - 1].split()
    if command[0] == 'potion':
        potion_amount = int(command[1])
        current_hp, amount_to_heal = potion(current_hp, initial_health, potion_amount)
        print(f'You healed for {amount_to_heal} hp.\nCurrent health: {current_hp} hp.')
    elif command[0] == 'chest':
        initial_bitcoin += int(command[1])
        print(f'You found {int(command[1])} bitcoins.')
    else:
        beast = command[0]
        damage_dealt = int(command[1])
        current_hp = damage(current_hp, damage_dealt)
        if current_hp == 0:
            print(f'You died! Killed by {beast}.\nBest room: {room}')
            break
        else:
            print(f'You slayed {beast}.')
else:
    print(f'You\'ve made it!\nBitcoins: {initial_bitcoin}\nHealth: {current_hp}')
