couples = int(input())

previous_sum = int(input()) + int(input())

max_difference = 0

for i in range(couples - 1):
    current_sum = int(input()) + int(input())
    current_diff = abs(previous_sum - current_sum)
    if current_diff > max_difference:
        max_difference = current_diff
    previous_sum = current_sum

if max_difference == 0:
    print(f'Yes, value={previous_sum}')
else:
    print(f'No, maxdiff={max_difference}')
