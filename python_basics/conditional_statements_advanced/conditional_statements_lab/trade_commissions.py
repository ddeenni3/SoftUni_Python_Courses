town = input()
sales_volume = float(input())

commission = 0

is_input_correct = True

if town == 'Sofia':
    if 0 <= sales_volume <= 500:
        commission = 0.05
    elif 500 < sales_volume <= 1000:
        commission = 0.07
    elif 1000 < sales_volume <= 10000:
        commission = 0.08
    elif sales_volume > 10000:
        commission = 0.12
    else:
        is_input_correct = False

elif town == 'Varna':
    if 0 <= sales_volume <= 500:
        commission = 0.045
    elif 500 < sales_volume <= 1000:
        commission = 0.075
    elif 1000 < sales_volume <= 10000:
        commission = 0.1
    elif sales_volume > 10000:
        commission = 0.13
    else:
        is_input_correct = False
elif town == 'Plovdiv':
    if 0 <= sales_volume <= 500:
        commission = 0.055
    elif 500 < sales_volume <= 1000:
        commission = 0.08
    elif 1000 < sales_volume <= 10000:
        commission = 0.12
    elif sales_volume > 10000:
        commission = 0.145
    else:
        is_input_correct = False
else:
    is_input_correct = False

total_sum = sales_volume * commission

if is_input_correct:
    print(f'{total_sum:.2f}')
else:
    print('error')
