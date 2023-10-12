wagons = int(input())

train = [0] * wagons

while True:
    command = input().split()
    if command[0] == 'End':
        break
    elif command[0] == 'add':
        train[-1] += int(command[1])
    elif command[0] == 'insert':
        index = int(command[1])
        train[index] += int(command[2])
    elif command[0] == 'leave':
        index = int(command[1])
        train[index] -= int(command[2])

print(train)
