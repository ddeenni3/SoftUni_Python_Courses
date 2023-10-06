def min_max_sum(numbers: list):
    return min(numbers), max(numbers), sum(numbers)


numbers_input = list(map(int, input().split()))

minimum_number, maximum_number, total_sum = min_max_sum(numbers_input)

print(f'The minimum number is {minimum_number}'
      f'\nThe maximum number is {maximum_number}'
      f'\nThe sum number is: {total_sum}')
