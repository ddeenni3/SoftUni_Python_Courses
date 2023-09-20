fruit_type = input()
day_of_week = input()
amount = float(input())

input_correct = True

price = 0

if day_of_week in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
    if fruit_type == 'banana':
        price = 2.50
    elif fruit_type == 'apple':
        price = 1.20
    elif fruit_type == 'orange':
        price = 0.85
    elif fruit_type == 'grapefruit':
        price = 1.45
    elif fruit_type == 'kiwi':
        price = 2.7
    elif fruit_type == 'pineapple':
        price = 5.50
    elif fruit_type == 'grapes':
        price = 3.85
    else:
        input_correct = False

elif day_of_week in ['Saturday', 'Sunday']:
    if fruit_type == 'banana':
        price = 2.70
    elif fruit_type == 'apple':
        price = 1.25
    elif fruit_type == 'orange':
        price = 0.9
    elif fruit_type == 'grapefruit':
        price = 1.6
    elif fruit_type == 'kiwi':
        price = 3
    elif fruit_type == 'pineapple':
        price = 5.6
    elif fruit_type == 'grapes':
        price = 4.2
    else:
        input_correct = False
else:
    input_correct = False

total = price * amount

if input_correct:
    print(f'{total:.2f}')
else:
    print('error')
