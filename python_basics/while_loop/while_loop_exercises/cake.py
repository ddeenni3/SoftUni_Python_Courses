cake_width = int(input())
cake_length = int(input())

cake_size = cake_length * cake_width

while cake_size > 0:
    command = input()
    if command == 'STOP':
        print(f'{cake_size} pieces are left.')
        break
    cake_size -= int(command)
else:
    print(f'No more cake left! You need {abs(cake_size)} pieces more.')
