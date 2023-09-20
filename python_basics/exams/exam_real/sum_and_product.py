n = int(input())
is_found = False

for num1 in range(1, 10):
    for num2 in range(9, num1, - 1):
        for num3 in range(0, 10):
            for num4 in range(9, num3, - 1):
                if (num1 + num2 + num3 + num4) == (num1 * num2 * num3 * num4) and n % 10 == 5:
                    print(f'{num1}{num2}{num3}{num4}')
                    is_found = True
                    break
                elif (num1 * num2 * num3 * num4) // (num1 + num2 + num3 + num4) == 3 and n % 3 == 0:
                    print(f'{num4}{num3}{num2}{num1}')
                    is_found = True
                    break
            if is_found:
                break
        if is_found:
            break
    if is_found:
        break

if not is_found:
    print(f'Nothing found')
    
