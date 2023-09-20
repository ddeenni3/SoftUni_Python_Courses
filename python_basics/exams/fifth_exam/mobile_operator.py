contract_length_yrs = input()
contract_type = input()
extra_mobile_data = input()
amount_of_months_to_pay = int(input())

price = 0

if contract_length_yrs == 'one':
    if contract_type == 'Small':
        price += 9.98
    elif contract_type == 'Middle':
        price += 18.99
    elif contract_type == 'Large':
        price += 25.98
    elif contract_type == 'ExtraLarge':
        price += 35.99
elif contract_length_yrs == 'two':
    if contract_type == 'Small':
        price += 8.58
    elif contract_type == 'Middle':
        price += 17.09
    elif contract_type == 'Large':
        price += 23.59
    elif contract_type == 'ExtraLarge':
        price += 31.79

if extra_mobile_data == 'yes':
    if price <= 10:
        price += 5.50
    elif price <= 30:
        price += 4.35
    else:
        price += 3.85

total = price * amount_of_months_to_pay

if contract_length_yrs == 'two':
    total *= 0.9625

print(f'{total:.2f} lv.')
