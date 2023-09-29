gifts = input().split()

while True:
    command = input()
    if command == 'No Money':
        break
    else:
        command_list = command.split()
        if command_list[0] == 'OutOfStock':
            gift = command_list[1]
            while gift in gifts:
                index = gifts.index(gift)
                gifts[index] = 'None'
        elif command_list[0] == 'Required':
            if 0 <= int(command_list[2]) < len(gifts):
                index = int(command_list[2])
                gifts[index] = command_list[1]
        elif command_list[0] == 'JustInCase':
            gifts[-1] = command_list[1]

while 'None' in gifts:
    gifts.remove('None')

print(' '.join(gifts))

