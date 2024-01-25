number_of_plants = int(input())

garden = {}

for plant in range(number_of_plants):
    name, rarity = input().split('<->')
    if name not in garden.keys():
        garden[name] = {'rarity': 0, 'rating': []}
    garden[name]['rarity'] += int(rarity)

while True:
    command = input()
    if command == 'Exhibition':
        break
    command = command.split(': ')
    if command[0] == 'Rate':
        current_name, rating = command[1].split(' - ')
        if current_name in garden.keys():
            garden[current_name]['rating'].append(int(rating))
        else:
            print('error')
    elif command[0] == 'Update':
        name, new_rarity = command[1].split(' - ')
        if name in garden.keys():
            garden[name]['rarity'] = int(new_rarity)
        else:
            print('error')
    elif command[0] == 'Reset':
        name = command[1]
        if name in garden.keys():
            garden[name]['rating'].clear()
        else:
            print('error')

print('Plants for the exhibition:')
for plant in garden:
    if garden[plant]['rating']:
        average_rating = sum(garden[plant]['rating']) / len(garden[plant]['rating'])
        print(f'- {plant}; Rarity: {garden[plant]["rarity"]}; Rating: {average_rating:.2f}')
    else:
        print(f'- {plant}; Rarity: {garden[plant]["rarity"]}; Rating: {0:.2f}')
