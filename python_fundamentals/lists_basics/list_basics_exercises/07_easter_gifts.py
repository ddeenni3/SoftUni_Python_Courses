gifts = input().split(' ')

while True:
    command = input()
    if command == 'No Money':
        break
    else:
        command_list = command.split(' ')
        if command_list[0] == 'OutOfStock':
            if command_list[1] in gifts:
                present = gifts[gifts.index(command_list[1])]
                while present in gifts:
                    gifts[gifts.index(present)] = 'None'

        elif command_list[0] == f'Required':
            if 0 <= int(command_list[2]) < len(gifts):
                gifts[int(command_list[2])] = command_list[1]
        elif command_list[0] == f'JustInCase':
            gifts[len(gifts) - 1] = command_list[1]

while 'None' in gifts:
    gifts.remove('None')

print(' '.join(gifts))
