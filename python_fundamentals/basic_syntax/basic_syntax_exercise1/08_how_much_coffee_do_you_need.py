coffee_counter = 0

command = input()

while command != 'END':
    if command.lower() in ['coding', 'cat', 'dog', 'movie']:
        if command.isupper():
            coffee_counter += 2
        else:
            coffee_counter += 1
    command = input()

if coffee_counter > 5:
    print('You need extra sleep')
else:
    print(coffee_counter)
    # elif command == 'dog' or command == 'cat':
    #     if command.isupper():
    #         coffee_counter += 2
    #     else:
    #         coffee_counter += 1
    # elif command == 'coding':
    #     if command.isupper():
    #         coffee_counter += 2
    #     else:
    #         coffee_counter += 1