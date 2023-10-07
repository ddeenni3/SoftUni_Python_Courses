def perfect_number(some_number: int) -> str:
    perfect_sum = 0
    for num in range(1, some_number):
        if some_number % num == 0:
            perfect_sum += num
    if some_number == perfect_sum:
        return 'We have a perfect number!'
    return 'It\'s not so perfect.'


number = int(input())

print(perfect_number(number))
