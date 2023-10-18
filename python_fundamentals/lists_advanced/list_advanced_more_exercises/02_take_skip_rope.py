input_string = list(input())

numbers = [int(num) for num in input_string if num.isdigit()]
string = [string for string in input_string if not string.isdigit()]
joined_string = ''.join(string)
take_numbers = [numbers[num - 1] for num in range(1, len(numbers) + 1) if num % 2 != 0]
skip_numbers = [numbers[num - 1] for num in range(1, len(numbers) + 1) if num % 2 == 0]

result_string = []
skip = 0
for action in range(len(take_numbers)):
    take_index = take_numbers[action]
    take = joined_string[skip:take_index + skip]
    result_string.append(take)
    skip += skip_numbers[action] + take_numbers[action]
print(''.join(result_string))
