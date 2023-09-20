a1 = int(input())
a2 = int(input())
n = int(input())

for num1 in range(a1, a2):
    if num1 % 2 == 0:
        continue
    for num2 in range(1, n):
        for num3 in range(1, int(n / 2)):
            combined = num2 + num3 + num1
            if combined % 2 == 0:
                continue
            else:
                print(f'{chr(num1)}-{num2}{num3}{num1}')
            # for num4 in range(a1, a2):
            #     combined = num2 + num3 + num4
            #     if combined % 2 == 0:
            #         continue
            #     else:
            #         print(f'{chr(num1)}-{num2}{num3}{num4}')
            #


