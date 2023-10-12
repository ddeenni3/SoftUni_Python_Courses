def number_classification(numbers: list):
    positive = [x for x in numbers if x >= 0]
    negative = [x for x in numbers if x < 0]
    even = [x for x in numbers if x % 2 == 0]
    odd = [x for x in numbers if x % 2 != 0]
    return positive, negative, even, odd


some_numbers = list(map(int, input().split(', ')))

all_positive, all_negative, all_even, all_odd = number_classification(some_numbers)

print(f'Positive: {", ".join(list(map(str, all_positive)))}\n'
      f'Negative: {", ".join(list(map(str, all_negative)))}\n'
      f'Even: {", ".join(list(map(str, all_even)))}\n'
      f'Odd: {", ".join(list(map(str, all_odd)))}')
