first_number = int(input())
second_number = int(input())
operator = input()

result = 0
odd_even = 'odd'

if operator == '+':
    result += first_number + second_number
    if result % 2 == 0:
        odd_even = 'even'
elif operator == '-':
    result += first_number - second_number
    if result % 2 == 0:
        odd_even = 'even'
elif operator == '*':
    result += first_number * second_number
    if result % 2 == 0:
        odd_even = 'even'
elif operator == '/' and second_number != 0:
    result += first_number / second_number
elif operator == '%' and second_number != 0:
    result += first_number % second_number

if (operator == '/' or operator == '%') and second_number == 0:
    print(f'Cannot divide {first_number} by zero')
elif operator == '/':
    print(f'{first_number} / {second_number} = {result:.2f}')
elif operator == '%':
    print(f'{first_number} % {second_number} = {result}')
elif operator in ['+', '-', '*']:  # Can be operator == or operator == or operator ==
    print(f"{first_number} {operator} {second_number} = {result} - {odd_even}")
