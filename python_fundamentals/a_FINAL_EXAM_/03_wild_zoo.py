zoo = {}
hungry_animals_per_area = {}

while True:
    command = input().split(': ')
    if command[0] == 'EndDay':
        break
    elif command[0] == 'Add':
        animal_info = command[1].split('-')
        name, needed_food, area = animal_info[0], int(animal_info[1]), animal_info[2]
        if name not in zoo.keys():
            zoo[name] = {'needed_food': 0, 'area': ''}
        zoo[name]['needed_food'] += needed_food
        zoo[name]['area'] = area
    elif command[0] == 'Feed':
        animal_info = command[1].split('-')
        name, food = animal_info[0], int(animal_info[1])
        if name in zoo.keys():
            zoo[name]['needed_food'] -= food
            if zoo[name]['needed_food'] <= 0:
                del zoo[name]
                print(f'{name} was successfully fed')

for animal in zoo:
    if zoo[animal]['area'] not in hungry_animals_per_area.keys():
        hungry_animals_per_area[zoo[animal]['area']] = []
    hungry_animals_per_area[zoo[animal]['area']].append(animal)

print('Animals:')
for animal in zoo:
    print(f' {animal} -> {zoo[animal]["needed_food"]}g')

print('Areas with hungry animals:')
for area in hungry_animals_per_area:
    print(f'{area}: {len(hungry_animals_per_area[area])}')
