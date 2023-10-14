def number_classification(numbers: list):
    positive = [x for x in numbers if x >= 0]
    negative = [x for x in numbers if x < 0]
    even = [x for x in numbers if x % 2 == 0]
    odd = [x for x in numbers if x % 2 != 0]
    return [str(x) for x in positive], [str(x) for x in negative], [str(x) for x in even], [str(x) for x in odd]


some_numbers = list(map(int, input().split(', ')))

all_positive, all_negative, all_even, all_odd = number_classification(some_numbers)

print(f'Positive: {", ".join(all_positive)}\n'
      f'Negative: {", ".join(all_negative)}\n'
      f'Even: {", ".join(all_even)}\n'
      f'Odd: {", ".join(all_odd)}')
