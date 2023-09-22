
while True:
    house = ''
    command = input()
    if command == 'Voldemort':
        print('You must not speak of that name!')
        break
    elif command == 'Welcome!':
        print('Welcome to Hogwarts.')
        break
    else:
        if len(command) < 5:
            house = 'Gryffindor'
        elif len(command) == 5:
            house = 'Slytherin'
        elif len(command) == 6:
            house = 'Ravenclaw'
        elif len(command) > 6:
            house = 'Hufflepuff'
    print(f'{command} goes to {house}.')
