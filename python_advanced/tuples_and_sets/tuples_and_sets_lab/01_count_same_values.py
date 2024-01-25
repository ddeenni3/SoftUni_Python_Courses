numbers =[float(x) for x in input().split()]

occurrences = {}

for number in numbers:
    occurrences[number] = numbers.count(number)

for number, occurrence in occurrences.items():
    print(f'{number:.1f} - {occurrence} times')