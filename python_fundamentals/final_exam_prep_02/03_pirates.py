cities = {}

while True:
    command = input().split("||")
    if command[0] == 'Sail':
        break
    city, population, gold = command[0], int(command[1]), int(command[2])
    if city not in cities.keys():
        cities[city] = {'population': 0, 'gold': 0}
    cities[city]['population'] += population
    cities[city]['gold'] += gold

while True:
    command = input().split('=>')
    if command[0] == 'End':
        break
    elif command[0] == 'Plunder':
        town = command[1]
        people = int(command[2])
        gold = int(command[3])
        cities[town]['population'] -= people
        cities[town]['gold'] -= gold
        print(f'{town} plundered! {gold} gold stolen, {people} citizens killed.')
        if cities[town]['population'] == 0 or cities[town]['gold'] == 0:
            print(f'{town} has been wiped off the map!')
            cities.pop(town)
    elif command[0] == 'Prosper':
        town = command[1]
        gold = int(command[2])
        if gold < 0:
            print('Gold added cannot be a negative number!')
        else:
            cities[town]['gold'] += gold
            print(f'{gold} gold added to the city treasury. {town} now has {cities[town]["gold"]} gold.')

count = len(cities)

if count > 0:
    print(f'Ahoy, Captain! There are {count} wealthy settlements to go to:')
    for city in cities:
        print(f'{city} -> Population: {cities[city]["population"]} citizens, Gold: {cities[city]["gold"]} kg')
else:
    print('Ahoy, Captain! All targets have been plundered and destroyed!')
