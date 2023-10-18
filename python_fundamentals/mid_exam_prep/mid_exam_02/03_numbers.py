def number_modifier(some_numbers: list):
    average_num = sum(some_numbers) // len(some_numbers)
    result = [x for x in some_numbers if x > average_num]
    sorted_result = sorted(result, reverse=True)
    return sorted_result


numbers = [int(x) for x in input().split()]

sorted_numbers = number_modifier(numbers)

if not sorted_numbers:
    print('No')
else:
    if len(sorted_numbers) <= 5:
        print(* sorted_numbers, sep=' ')
    elif len(sorted_numbers) > 5:
        index = 0
        for num in range(5):
            print(sorted_numbers[index], end=' ')
            index += 1
