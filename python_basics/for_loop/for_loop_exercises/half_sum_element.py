import sys

num = int(input())
total_sum = 0
max_number = -sys.maxsize

for _ in range(num):
    number = int(input())
    if number > max_number:
        max_number = number
    total_sum += number

total_sum -= max_number
if total_sum == max_number:
    print('Yes')
    print(f'Sum = {max_number}')
else:
    print('No')
    print(f'Diff = {abs(total_sum - max_number)}')
