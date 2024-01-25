guests = [input() for _ in range(int(input()))]

while True:
    command = input()
    if command == 'END':
        break
    if command in guests:
        guests.remove(command)

print(len(guests))
guests = sorted(guests)
print(*guests, sep='\n')