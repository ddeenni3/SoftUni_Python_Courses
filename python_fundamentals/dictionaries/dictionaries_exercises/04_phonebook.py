phonebook = {}

while True:
    command = input()
    if '-' not in command:
        break
    name, number = command.split('-')
    phonebook[name] = number

search_amount = int(command)

for search in range(search_amount):
    search_name = input()
    if search_name in phonebook.keys():
        print(f'{search_name} -> {phonebook[search_name]}')
    else:
        print(f'Contact {search_name} does not exist.')
