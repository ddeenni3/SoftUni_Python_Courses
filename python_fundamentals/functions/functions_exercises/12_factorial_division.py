def factorial_num(number: int):
    factorial = number
    for num in range(2, number):
        factorial *= num
    return factorial


first_number = int(input())
second_number = int(input())

first_number_factorial = factorial_num(first_number)
second_number_factorial = factorial_num(second_number)

result = first_number_factorial / second_number_factorial

print(f'{result:.2f}')
