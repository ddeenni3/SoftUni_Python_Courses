n1 = int(input())
n2 = int(input())
total_combinations_allowed = int(input())

combinations_counter = 0
num1 = 35
num2 = 64

break_flag = False

for num3 in range(1, n1 + 1):
    for num4 in range(1, n2 + 1):
        if combinations_counter == total_combinations_allowed:
            break_flag = True
            break
        else:
            print(f'{chr(num1)}{chr(num2)}{num3}{num4}{chr(num2)}{chr(num1)}|', end='')
            combinations_counter += 1
            num1 += 1
            num2 += 1
            if num1 > 55:
                num1 = 35
            if num2 > 96:
                num2 = 64
    if break_flag:
        break

