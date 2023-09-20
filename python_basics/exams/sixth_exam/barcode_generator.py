starting_interval = input()
ending_interval = input()

for num1 in range(int(starting_interval[0]), int(ending_interval[0]) + 1):
    for num2 in range(int(starting_interval[1]), int(ending_interval[1]) + 1):
        for num3 in range(int(starting_interval[2]), int(ending_interval[2]) + 1):
            for num4 in range(int(starting_interval[3]), int(ending_interval[3]) + 1):
                if num1 % 2 != 0 and num2 % 2 != 0 and num3 % 2 != 0 and num4 % 2 != 0:
                    print(f'{num1}{num2}{num3}{num4}', end=' ')
