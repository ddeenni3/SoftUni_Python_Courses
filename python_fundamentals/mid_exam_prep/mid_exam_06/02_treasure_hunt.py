initial_loot = input().split('|')
current_command = input()
while current_command != 'Yohoho!':
    command, *items = [x for x in current_command.split()]
    if command == 'Loot':
        for item in items:
            if item not in initial_loot:
                initial_loot.insert(0, item)
    elif command == 'Drop':
        index = int(items[0])
        if 0 <= index < len(initial_loot):
            initial_loot.append(initial_loot.pop(index))
    elif command == 'Steal':
        count = int(items[0])
        stolen = initial_loot[-count:]
        initial_loot = initial_loot[:-count]
        print(*stolen, sep=', ')
    current_command = input()
if initial_loot:
    total_points = sum(len(x) for x in initial_loot) / len(initial_loot)
    print(f'Average treasure gain: {total_points:.2f} pirate credits.')
else:
    print('Failed treasure hunt.')
