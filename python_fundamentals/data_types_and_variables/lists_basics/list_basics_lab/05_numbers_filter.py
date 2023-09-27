n = int(input())

combined = []

for _ in range(n):
    number = int(input())
    combined.append(number)

command = input()
filtered = []

for element in combined:
    if command == 'even':
        if element % 2 == 0:
            filtered.append(element)
    elif command == 'odd':
        if element % 2 != 0:
            filtered.append(element)
    elif command == 'positive':
        if element >= 0:
            filtered.append(element)
    elif command == 'negative':
        if element < 0:
            filtered.append(element)
print(filtered)
    