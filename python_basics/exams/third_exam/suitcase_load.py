trunk_capacity = float(input())

counter = 0

while True:
    command = input()
    if command == 'End':
        print(f'Congratulations! All suitcases are loaded!')
        break
    package = float(command)
    counter += 1
    if counter % 3 == 0:
        package *= 1.10
    trunk_capacity -= package
    if trunk_capacity <= 0:
        counter -= 1
        print('No more space!')
        break

print(f'Statistic: {counter} suitcases loaded.')
