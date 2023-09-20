total_sum = 0

while True:
    command = input()
    if command == 'NoMoreMoney':
        break
    else:
        command = float(command)
        if command < 0:
            print('Invalid operation!')
            break
        print(f'Increase: {command:.2f}')
        total_sum += command


print(f'Total: {total_sum:.2f}')
