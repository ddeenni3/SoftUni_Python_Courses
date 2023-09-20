starting_interval_first = int(input())
starting_interval_second = int(input())
diff_first = int(input())
diff_second = int(input())

for num1 in range(starting_interval_first, (starting_interval_first + diff_first) + 1):
    for num2 in range(starting_interval_second, (starting_interval_second + diff_second) + 1):
        is_prime = True
        for i in range(2, num1):
            if num1 % i == 0:
                is_prime = False
                break
        for x in range(2, num2):
            if num2 % x == 0:
                is_prime = False
                break
        if is_prime:
            print(f'{num1}{num2}')
