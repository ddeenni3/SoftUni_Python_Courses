def calculations(operator: str, a: int, b: int):
    if operator == 'multiply':
        return a * b
    elif operator == 'divide':
        if b == 0:
            return 'Cannot divide by 0'
        else:
            return int(a / b)
    elif operator == 'add':
        return a + b
    elif operator == 'subtract':
        return a - b


action = input()
first_number = int(input())
second_number = int(input())

print(calculations(action, first_number, second_number))

