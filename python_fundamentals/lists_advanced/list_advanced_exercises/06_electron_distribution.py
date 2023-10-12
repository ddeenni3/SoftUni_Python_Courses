number_of_electrons = int(input())

result = []
n = 1
while number_of_electrons > 0:
    current_number = 2 * (n ** 2)
    if number_of_electrons - current_number > 0:
        number_of_electrons -= current_number
        result.append(current_number)
    else:
        current_number = number_of_electrons
        result.append(current_number)
        number_of_electrons -= current_number
    n += 1

print(result)
