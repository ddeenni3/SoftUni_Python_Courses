drink = input()
sugar = input()
amount = int(input())
price = 0

if drink == 'Espresso':
    if sugar == 'Without':
        price += amount * 0.90
        price *= 0.65
    elif sugar == 'Normal':
        price += amount * 1
    elif sugar == 'Extra':
        price += amount * 1.20
    if amount >= 5:
        price *= 0.75
if drink == 'Cappuccino':
    if sugar == 'Without':
        price += amount * 1
        price *= 0.65
    elif sugar == 'Normal':
        price += amount * 1.20
    elif sugar == 'Extra':
        price += amount * 1.60
if drink == 'Tea':
    if sugar == 'Without':
        price += amount * 0.5
        price *= 0.65
    elif sugar == 'Normal':
        price += amount * 0.6
    elif sugar == 'Extra':
        price += amount * 0.7
if price > 15:
    price *= 0.8

print(f'You bought {amount} cups of {drink} for {price:.2f} lv.')

