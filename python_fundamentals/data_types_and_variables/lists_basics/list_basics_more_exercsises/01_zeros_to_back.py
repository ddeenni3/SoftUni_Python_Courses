numbers = input().split(', ')
amount_of_zeros = numbers.count('0')
for zero in range(amount_of_zeros):
    numbers.remove('0')
    numbers.append('0')
integer_numbers = [int(num) for num in numbers]
print(integer_numbers)
