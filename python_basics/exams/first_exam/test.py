low_limit = (input())
high_limit = (input())

for num1 in range(int(low_limit[0]), int(high_limit[0]) + 1):
    for num2 in range(int(low_limit[1]), int(high_limit[1]) + 1):
        for num3 in range(int(low_limit[2]), int(high_limit[2]) + 1):
            for num4 in range(int(low_limit[3]), int(high_limit[3]) + 1):
                if num1 % 2 != 0 and num2 % 2 != 0 and num3 != 0 and num4 != 0:
                    print(f'{num1}{num2}{num3}{num4}', end=' ')
