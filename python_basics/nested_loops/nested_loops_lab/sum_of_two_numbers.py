starting_interval = int(input())
ending_interval = int(input())
magic_number = int(input())

combination_counter = 0

combination_found = False

for x in range(starting_interval, ending_interval + 1):
    for y in range(starting_interval, ending_interval + 1):
        combination_counter += 1
        if x + y == magic_number:
            combination_found = True
            print(f'Combination N:{combination_counter} ({x} + {y} = {magic_number})')
            break
    if combination_found:
        break

if not combination_found:
    print(f'{combination_counter} combinations - neither equals {magic_number}')
