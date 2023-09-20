import sys

n = int(input())
sum_even = 0
max_num_even = -sys.maxsize
min_num_even = sys.maxsize

sum_odd = 0
max_num_odd = -sys.maxsize
min_num_odd = sys.maxsize

for i in range(1, n + 1):
    number = float(input())
    if i % 2 == 0:
        sum_even += number
        if number > max_num_even:
            max_num_even = number
        if number < min_num_even:
            min_num_even = number
    else:
        sum_odd += number
        if number > max_num_odd:
            max_num_odd = number
        if number < min_num_odd:
            min_num_odd = number

print(f'OddSum={sum_odd:.2f},')
if min_num_odd != sys.maxsize:
    print(f'OddMin={min_num_odd:.2f},')
else:
    print('OddMin=No,')
if max_num_odd != -sys.maxsize:
    print(f'OddMax={max_num_odd:.2f},')
else:
    print('OddMax=No,')
print(f'EvenSum={sum_even:.2f},')
if min_num_even != sys.maxsize:
    print(f'EvenMin={min_num_even:.2f},')
else:
    print('EvenMin=No,')
if max_num_even != -sys.maxsize:
    print(f'EvenMax={max_num_even:.2f}')
else:
    print('EvenMax=No')
