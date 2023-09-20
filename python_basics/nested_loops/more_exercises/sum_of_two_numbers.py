starting_interval = int(input())
ending_interval = int(input())
magic_num = int(input())

combination_counter = 0

break_flag = False

for x in range(starting_interval, ending_interval + 1):
    for y in range(starting_interval, ending_interval + 1):
        combination_counter += 1
        if x + y == magic_num:
            print(f'Combination N:{combination_counter} ({x} + {y} = {magic_num})')
            break_flag = True
            break
    if break_flag:
        break
if not break_flag:
    print(f'{combination_counter} combinations - neither equals {magic_num}')



