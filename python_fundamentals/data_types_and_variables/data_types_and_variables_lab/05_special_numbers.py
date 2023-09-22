number = int(input())

for n in range(1, number + 1):
    total = 0
    for y in str(n):
        total += int(y)
    special_number = False
    if total == 5 or total == 11 or total == 7:
        special_number = True

    print(f'{n} -> {special_number}')

