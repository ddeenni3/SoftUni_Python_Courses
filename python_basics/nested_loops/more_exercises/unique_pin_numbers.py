first_num_end_interval = int(input())
second_num_end_interval = int(input())
third_num_end_interval = int(input())

first_num = 0
second_num = 0
third_num = 0

for x in range(1, first_num_end_interval + 1):
    if x % 2 != 0:
        continue
    else:
        first_num = x
    for y in range(2, second_num_end_interval + 1):
        is_prime = True
        for num in range(2, y):
            if y % num == 0:
                is_prime = False
                break
        if not is_prime:
            continue
        else:
            second_num = y
        for z in range(1, third_num_end_interval + 1):
            if z % 2 != 0:
                continue
            else:
                third_num = z
                print(f'{first_num} {second_num} {third_num}')

