n = int(input())
current_number = 1

is_finished = False

for i in range(1, n + 1):
    for y in range(1, i + 1):
        print(current_number, end=' ')
        current_number += 1
        if current_number > n:
            is_finished = True
            break
    if is_finished:
        break
    print()
