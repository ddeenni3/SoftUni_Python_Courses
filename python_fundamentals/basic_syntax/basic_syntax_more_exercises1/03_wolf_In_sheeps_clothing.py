heard = input()

list_heard = heard.split(', ')

list_heard.reverse()

if list_heard[0] == 'wolf':
    print('Please go away and stop eating my sheep')
else:
    for position in range(len(list_heard)):
        if list_heard[position] == 'wolf':
            print(f'Oi! Sheep number {position}! You are about to be eaten by a wolf!')
            break

