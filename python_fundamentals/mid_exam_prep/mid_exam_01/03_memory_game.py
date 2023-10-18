elements = [x for x in input().split()]
number_of_moves = 0
user_won = False

while True:
    command = input()
    if command == 'end':
        break
    current_command = command.split()
    first_index = int(current_command[0])
    second_index = int(current_command[1])
    number_of_moves += 1
    if first_index == second_index or first_index < 0 or second_index > len(elements) - 1 \
            or len(elements) - 1 < first_index or 0 > second_index:
        print('Invalid input! Adding additional elements to the board')
        elements.insert(len(elements) // 2, f'-{str(number_of_moves)}a')
        elements.insert(len(elements) // 2, f'-{str(number_of_moves)}a')
    else:
        if elements[first_index] == elements[second_index]:
            found_element = elements[first_index]
            print(f'Congrats! You have found matching elements - {elements[first_index]}!')
            while found_element in elements:
                elements.remove(found_element)
            if len(elements) == 0:
                print(f'You have won in {number_of_moves} turns!')
                user_won = True
                break
        elif elements[first_index] != elements[second_index]:
            print('Try again!')
    if user_won:
        break

if len(elements) > 0:
    print(f'Sorry you lose :(\n'
          f'{" ".join(elements)}')
