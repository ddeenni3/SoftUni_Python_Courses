starting_interval = int(input())
ending_interval = int(input())

for num1 in range(starting_interval, ending_interval + 1):
    for num2 in range(starting_interval, ending_interval + 1):
        for num3 in range(starting_interval, ending_interval + 1):
            for num4 in range(starting_interval, ending_interval + 1):
                if num1 % 2 == 0 and num4 % 2 != 0:
                    if num1 > num4:
                        if (num2 + num3) % 2 == 0:
                            print(f'{num1}{num2}{num3}{num4}', end=' ')
                elif num1 % 2 != 0 and num4 % 2 == 0:
                    if num1 > num4:
                        if (num2 + num3) % 2 == 0:
                            print(f'{num1}{num2}{num3}{num4}', end=' ')
                else:
                    continue
