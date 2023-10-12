def even_indices(numbers: list) -> list:
    evens_list = [x for x in range(len(numbers)) if numbers[x] % 2 == 0]

    return evens_list


some_numbers = list(map(int, input().split(', ')))

print(even_indices(some_numbers))

