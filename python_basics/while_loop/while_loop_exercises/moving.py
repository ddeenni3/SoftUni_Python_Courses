space_width = int(input())
space_length = int(input())
space_height = int(input())

space_volume = space_width * space_height * space_length

while space_volume > 0:
    command = input()
    if command == 'Done':
        print(f'{space_volume} Cubic meters left.')
        break
    space_volume -= int(command)

if space_volume <= 0:
    print(f'No more free space! You need {abs(space_volume)} Cubic meters more.')

